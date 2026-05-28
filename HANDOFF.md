# HANDOFF — OmegaWiki (documento vivo)
> Última consolidación: 2026-05-28. Doc para arrancar una conversación nueva con todo el contexto.
> El histórico cronológico previo a esta fecha está en HANDOFF_archive_2026-05-28.md.

## 1. QUÉ ES ESTO + DIVERGENCIAS DEL ORIGINAL

OmegaWiki = grafo de conocimiento de papers científicos en Markdown, gestionado con
Claude Code. Entidades: **papers, claims** (afirmaciones atómicas tipadas), **concepts,
foundations** (métodos/técnicas), **people**, y **edges** (relaciones en graph/edges.jsonl).
Repo: PepCalafell/OmegaWiki (rama main).

**Divergencias respecto a OmegaWiki v0.1.0 (vanilla):**
- El cambio está concentrado en el **skill de ingest**, no en la estructura. Se mantuvo
  el esqueleto original (mismos 9 Steps, misma organización) y se reescribió el CONTENIDO
  para biomedicina. Medido: Step 4 (concepts/claims/people) pasó de 10 líneas (genérico)
  a 88 (esquema biomédico); el SKILL completo de 267 a 362 líneas.
- Adaptación biomédica: claims tipados (mechanistic/methodological/correlational/
  quantitative/pharmacological), enums de estado, people con relevance_tier, foundations,
  identidad por PubMed/DOI/PMID en vez de arXiv, aliases estrictos.
- **DOS COPIAS del skill conviven:**
  - `.claude/skills/ingest/` = **VIVA, FUENTE DE VERDAD.** La adaptación biomédica.
  - `i18n/en/skills/ingest/` = vestigio del original vanilla. **MUERTA.** No se toca, no se sincroniza.
  - ⚠️ `setup.sh` Step 3b (copiaba i18n/ → .claude/) está NEUTRALIZADO/comentado a propósito,
    para que no sobrescriba la viva con la vanilla. **NUNCA correr setup.sh esperando que sincronice skills.**

## 2. FLUJO DE TRABAJO

1. `.venv/bin/python scripts/next_paper.py` — qué paper toca (ver Bug next_paper en §5).
2. `/ingest "ruta.pdf"` en Claude Code (Opus, medium effort).
3. `./scripts/verify_paper.sh <slug>` — **con slug explícito** (ver §5 bug mtime, resuelto).
   Esperar a **0🔴**. El bloque 4 (duplicados) es 🟡 y NO bloquea.
4. `./scripts/commit_paper.sh` — pide TÍTULO y CUERPO.
   - Cuerpo: RECORTAR el ruido de Claude Code (`✻ Crunched...`, `※ recap:...`).
   - **TÍTULO sin "#N"** (ver decisión en §4): `ingest: Autor AÑO Venue — título`.
   - Leer el ">>> Mensaje completo" ANTES de confirmar (caza deslices de título).

**REGLA DE ORO:** nunca commitear con verify en 🔴. Un paper, verificado, commiteado, y el
siguiente. NO encadenar ingests sin verificar. Revisar edges paper-a-paper (destinos
existen) y, en papers fuera del núcleo, leer los claims con lupa semántica (ver §5).

## 3. ESTADO ACTUAL

- **56 papers · 1075 claims · 364 conceptos · ~2387 edges**
- Lint: 0🔴 0🟡. Todo commiteado y pusheado. HEAD `54ba110`.
- Últimos ingests: #48 VHL, #50 DECODE, #51 DHPS, #52 cytokine dictionary,
  #53 skin fibroblast atlas, #54 AlphaCell, #55 effector-host interactome.
- People tiers: 168 emerging · 1 established (Ginhoux, 4 papers) · 2 core (Ballestar,
  Calafell — manual_override). Regla: ≥10 core, ≥4 established, resto emerging.

## 4. DECISIONES DE DISEÑO TOMADAS (no reabrir sin dato nuevo)

- **Aliases estrictos** (Sección B del SKILL): aliases = solo sinónimos estrictos.
  Validado en ~17 ingests: 0 conceptos duplicados. Evita colisiones en find-similar-concept.
- **.claude = fuente de verdad, setup.sh neutralizado** (ver §1).
- **Bug 2 (enums) — NO se hace autofix.** Inventario dio 1 enum inválido vivo en ~1700
  entidades. El método manual (lint caza 🔴 → corregir → commit) caza el 100%. Autofix sería
  mantenimiento perpetuo por ~3 min/ingest. En su lugar, CLEANING PERIÓDICO (cada ~10 papers):
    - `grep -rh "^status:" wiki/foundations/*.md | sort | uniq -c`
    - `grep -rh "^status:" wiki/claims/*.md | sort | uniq -c`
    - `grep -rh "^maturity:" wiki/concepts/*.md | sort | uniq -c`
    - `grep -rh "^relevance_tier:" wiki/people/*.md | sort | uniq -c`
- **Títulos de commit SIN "#N".** El #N viene del orden de next_paper.py, que NO es estable.
  Identificadores estables (slug/DOI/PMID) ya van en el cuerpo. Títulos viejos con #N o
  paréntesis sueltos NO se reescriben (pusheados; no vale push --force por cosmética).
- **Aliases viejos: estrategia REACTIVA.** No limpiar los ~247 conceptos viejos
  proactivamente. El check de duplicados marca colisiones cuando ocurren; se limpia entonces,
  con el recuento de aliases como pista de cuál es el viejo.
- **Tiers de people: el ingest SUGIERE, no aplica.** Emite "PEOPLE TIER CHANGE SUGGESTED";
  se actualiza a mano. manual_override se respeta.

## 5. BUGS CATALOGADOS

- **Bug 2 — enums inválidos.** Frecuente, no universal (~3 de cada 6 ingests). El verify lo
  caza siempre (🔴), corrección manual. 'emerging' en foundations.status es el caso
  recurrente. DECISIÓN: sin autofix (§4). Enums válidos:
  foundations.status {mainstream,historical} · claims.status {proposed,weakly_supported,
  supported,challenged,deprecated} · concepts.maturity {stable,active,emerging,deprecated} ·
  people.relevance_tier {emerging,established,core}.
  HALLAZGO DE DISEÑO (no urgente): foundations.status no tiene casilla para "establecido pero
  reciente" (424 mainstream / 2 historical). Valorar ampliar el enum → mataría el 'emerging' recurrente.
- **Bug 3 — foundations con esquema inventado** (type/category en vez de domain/status).
  Corregir a mano si aparece.
- **Bug 6 — xref-asymmetry en lint.py — PARCIAL.** Rama people→paper RESUELTA (L325 ahora
  acepta reverse-link con o sin prefijo papers/; probado con no-regresión). PENDIENTE: mismo
  bug de prefijo probable en ramas concepts (~L313) e ideas (~L355) — arreglar con helper
  normaliza_wikilink() cuando haya caso real, NO a ciegas (riesgo de falsos negativos al
  refactorizar el corazón del linter). PENDIENTE: relevance_tier no se valida por lint.
- **Bug del 'tags' — PATRÓN confirmado.** El ingest omite el campo `tags` (requerido) en
  conceptos, en papers que crean MUCHOS conceptos de golpe (#46: 8 conceptos; #55: 7). Da
  8🔴/7🔴 missing-field. Arreglo a mano (set base de dominio + matiz por concepto). Candidato
  a arreglo en el SKILL (Step 4 debe exigir tags).
- **Bug next_paper.py — empareja por slug del nombre de PDF, no del título.** Re-ofrece papers
  ya ingestados cuando el nombre del archivo difiere del título. Workaround: KNOWN_ALIASES
  (parcheado caso a caso; tasa ~1/8, sostenible). Arreglo de raíz (comparar por DOI/título):
  baja prioridad.
- **Fallos de enlazado — el ingest es flojo con reverse-links y enlaces a destinos inexistentes.**
  Casos: #36 ([[topics/]] vacío + reverse-link a medias), #40 (edge+wikilink a paper no
  ingestado), #45 (wikilink a paper no ingestado DENTRO del cuerpo de un claim). El SKILL
  ahora exige verificar existencia del destino para edges y Related, pero NO cubre todas las
  ubicaciones (prosa de claims). El lint SÍ caza dangling-edge y broken-link (🟡). La red
  fiable sería un check dedicado que recorra TODOS los wikilinks.
- **type/status de claims NO estructurado (hallazgo #54).** El tipo (mechanistic/etc.) vive
  SOLO inline en el bullet del paper, no en un campo del frontmatter del claim. No se puede
  consultar/filtrar/validar. Además, el bullet inline y el frontmatter del claim NO se
  sincronizan (al recalibrar un claim se cambia el frontmatter, el bullet queda viejo).
  DECISIÓN PENDIENTE: ¿hacer `type` campo real del frontmatter?

## 6. DEUDA PENDIENTE PRIORIZADA (sesión de tooling)

1. **commit_paper.sh autogenere/valide el TÍTULO** desde el frontmatter del paper (autor/año/
   venue/título limpios) y el usuario solo confirme. 4 deslices ya (#43,#50,#52,#54). Subida.
2. **Bug del 'tags' en el SKILL** — que el Step 4 exija `tags` al crear conceptos. Ya es patrón.
3. **Completar Bug 6** — ramas concepts/ideas (con caso real) + validación de relevance_tier
   y de type/status de claims en lint. Idealmente helper normaliza_wikilink().
4. **Check de enlazado dedicado** — recorre TODOS los wikilinks (claims, conceptos, prosa),
   no solo edges/Related. La red fiable frente a los fallos de enlazado.
5. **remove-edge en research_wiki.py** — no existe; borrar un edge requiere editar
   edges.jsonl a mano.
6. **Decisión enum foundations.status** — ¿añadir valor "establecido pero reciente"? Mata la
   causa raíz del 'emerging'. Tocar enum = validador + lint + documentar. Su propia sesión.
7. **Auditoría semántica formal** — leer claims contra PDF en ~5 papers, medir tasa de error
   de atribución. El verify valida que los claims estén bien FORMADOS, no que digan la verdad.
8. **foundations: 350+** — ¿la sección C del SKILL sobre-crea foundations de un solo paper?
9. **Formato [cnn] vs [slug] en claims** — decisión abierta de migración. Sesión propia.
10. **Consolidar este handoff periódicamente** (como hoy) si vuelve a crecer por acumulación.
11. **validate_step4e.py** da traceback crudo ante argumento inválido. Menor.
12. **i18n/ obsoleto** — vestigio del original; marcar/congelar (ver §1).

## 7. FALSOS POSITIVOS PERMANENTES del bloque 4 (ignorar SIEMPRE)

1. Claims Novae breast/colon (ratio 0.95) — dos benchmarks reales distintos.
2. Conceptos immune-checkpoint-blockade (13 aliases) vs innate-immune-checkpoint-blockade
   (2 aliases) — vecinos legítimos (ICB adaptativo de células T vs checkpoints innatos
   mieloides CD47/SIRPA/LILRB). Confirmado por definiciones. NO fusionar.

## 8. PRIMERAS ACCIONES PRÓXIMA SESIÓN

1. `git pull && git log --oneline -5 && git status` — confirmar estado.
2. `./scripts/verify_paper.sh` (modo fecha, mostrará [AVISO]) → confirmar 0🔴 global.
3. Decidir: seguir ingestando (flujo §2) o sesión de tooling (deuda §6, empezar por #1 o #2).
   Recomendación: una sesión de tooling rinde — afila el hacha para los ~40 papers que quedan.
