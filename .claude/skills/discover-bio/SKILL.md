---
name: discover-bio
description: >
  Dada una pregunta de investigacion, abanica la busqueda sobre PubMed (y
  Consensus si esta conectado como MCP), dedupea y rankea candidatos por acuerdo
  entre fuentes + recencia, marca accesibilidad (OA via PMC vs paywall) y
  comprueba si cada candidato ya esta en el vault (wiki/papers/). Es la etapa de
  DESCUBRIMIENTO biomedica del pipeline: propone una cola de candidatos que el
  usuario revisa; NO descarga ni ingiere nada.
  Usar cuando el usuario quiere encontrar papers sobre un tema biomedico o llenar
  un hueco concreto de su biblioteca (gap-loop). Invocar explicitamente como
  `/discover-bio "<pregunta>"`.
---

# /discover-bio — descubrimiento biomedico con corroboracion cruzada

## Relacion con /discover (sin colision)
Esta skill vive en `.claude/skills/discover-bio/` y es INDEPENDIENTE del
`/discover` del paquete OmegaWiki (S2/anchor, respaldado por `tools/discover.py`
y cableado en `/ingest --discover`). No se borra ni se modifica nada del repo:
- `/discover`     -> S2/anchor, "que leo despues de este paper". Intacto.
- `/discover-bio` -> PubMed/pregunta, "que bajo para llenar este hueco". Esta.
Se invocan por nombre distinto, asi que no hay conflicto.

## Objetivo
Dada una pregunta de investigacion, devolver una **cola de candidatos rankeada**
que el usuario revisa ANTES de descargar nada. El ranking usa la senal de
**repeticion entre fuentes independientes** (un paper que aparece en varias
fuentes es probablemente central) + recencia, marca accesibilidad y si el paper
ya esta en el vault.

Principio que no se viola: esto solo PRIORIZA que bajar. La verificacion
cientifica real la dan el PDF descargado + las notas, nunca el acuerdo entre IAs.

## Entrada
- `question`: pregunta en lenguaje natural (p.ej. "macrofagos en hipoxia
  asociados a p65"). Puede venir de una open question del Gap Map (wiki/) o
  escribirse a mano para un hueco concreto destapado al escribir.
- `vault_path` (opcional): ruta del vault. Por defecto: `wiki/papers/`
  (relativa a la raiz del repo).

## Pasos

1. **Genera 2-3 angulos de query.** NO metas todos los terminos con AND (PubMed
   devuelve 0). Empieza ancho y combina. Ejemplo para la pregunta de p65:
   - `macrophage hypoxia epigenetic`
   - `macrophage hypoxia NF-kB`
   - `hypoxia macrophage DNA demethylation TET`

2. **PubMed** (MCP `PubMed:search_articles`, `sort=relevance`, `max_results=15`
   por angulo; anade un pase con `sort=pub_date` para capturar lo mas reciente).
   Para cada hit recoge: pmid, titulo, DOI, journal, ano, y PMC (si hay PMC, es
   open access). Usa `PubMed:get_article_metadata` para los detalles.

3. **Consensus** (si esta conectado como MCP en Claude Code): pasa la MISMA
   pregunta y recoge los papers y su senal de acuerdo. Si NO esta conectado,
   saltalo y dilo explicitamente en la salida (no finjas que lo consultaste).
   Perplexity NO se cablea aqui (sin API usable, decision ya tomada): si quieres
   un cruce con Perplexity, hazlo a mano fuera de la skill y trae los DOIs.

4. **Dedupe** por DOI; si falta DOI, por titulo normalizado (minusculas, sin
   puntuacion).

5. **Ranking.** Para cada candidato calcula:
   - `n_fuentes`: en cuantas fuentes independientes aparece. ESTA es la senal de
     "consenso/verificacion de relevancia". Con solo PubMed sera siempre 1 y el
     ranking cae a recencia; conectar Consensus es lo que activa la senal.
   - `year`: recencia.
   Ordena por `n_fuentes` desc, luego `year` desc.

6. **Vault check.** Para cada candidato comprueba si ya esta en `vault_path`
   cruzando contra el frontmatter de `wiki/papers/*.md`, por DOI **y** por PMID
   (los papers biomedicos sin arXiv se reconocen por uno u otro):
   ```bash
   grep -rl "10.xxxx/yyyy" wiki/papers/      # por DOI
   grep -rl "pmid:.*12345678" wiki/papers/   # por PMID
   ```
   Si el repo ya tiene logica de dedup (la de `tools/discover.py --wiki-root` o
   `scripts/next_paper.py`), reusala en vez del grep para mayor robustez.
   Marca `ya_en_vault: si/no`. Los `no` con `n_fuentes` alto son la PRIORIDAD de
   descarga (= huecos reales).

7. **Accesibilidad.** PMC presente -> "OA (descarga directa de PMC)".
   Sin PMC -> "manual (plugin de la uni)".

## Salida (markdown)
Lista rankeada agrupada en tres bloques:
- **Prioridad de descarga** — `n_fuentes` alto y NO en vault.
- **Ya lo tienes** — en vault (para confirmar cobertura).
- **Baja confianza** — 1 sola fuente (revisar con criterio o descartar).

Formato por linea:
`[n_fuentes fuentes] Titulo — Journal Ano — DOI/PMID — accesibilidad — ya_en_vault`

Cierra con una nota recordando que esto es priorizacion, no verificacion, y que
el siguiente paso es BAJAR A MANO los elegidos del bloque "prioridad" (PMC
directo si es OA; plugin de la uni si es paywall) y luego `/ingest` sobre el PDF.
No existe ningun `/acquire` automatico: la descarga es manual.

## Atribucion
Si usas datos de PubMed, identificalo ("Datos de PubMed") e incluye los enlaces
DOI/PMID de los articulos citados.

## Notas de implementacion
- Skill agente-dirigida: tu (Claude Code) ejecutas los pasos llamando a los MCP
  conectados; no requiere script externo. Para discovery es aceptable (el output
  es un shortlist que el usuario revisa, no escrituras al vault). Si en algun
  momento quieres reproducibilidad/checkpoints, mueve el dedup+ranking a un
  script (a imagen de `tools/discover.py`) y deja la skill como orquestador.
- Requiere PubMed (y opcionalmente Consensus) configurados como MCP en Claude
  Code (ver MCP_SETUP). Con solo PubMed funciona igual, con `n_fuentes`=1.
