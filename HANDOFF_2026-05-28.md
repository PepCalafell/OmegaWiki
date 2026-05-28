# HANDOFF — OmegaWiki, sesión 2026-05-28

Documento para arrancar una conversación nueva con todo el contexto.

## Estado del wiki al cerrar

- papers: 38 · claims: 716 · concepts: 258 · foundations: 350+ · edges: 1642
- Lint: 0🔴 0🟡 al cerrar
- Rama: main, todo commiteado y pusheado a PepCalafell/OmegaWiki
- Últimos ingests: #70 Hamon 2025 (TREM2/HCC), #35 AHR host-pathogen

## Lo que ya está montado (sesiones 27-28 may)

### Check de duplicados
- `tools/check_duplicates.py` — duplicados léxicos de conceptos + duplicados
  intra-paper de claims. Integrado en `verify_paper.sh` BLOQUE 4. Es 🟡, NO
  bloquea el commit.
- Ahora muestra el recuento de aliases en colisiones de conceptos
  ("A: slug (11 aliases)") como pista de cuál limpiar. NO es un veredicto:
  aplicar el exclusivity test a mano.
- Limitación: solo caza duplicados LÉXICOS. NO ve el duplicado semántico
  con nombres distintos.
- Falso positivo conocido y ESPERADO: par de claims Novae breast/colon
  (ratio 0.95) — dos benchmarks reales distintos. Ignorar siempre.

### .claude/ es la FUENTE DE VERDAD — setup.sh neutralizado
- `.claude/skills/ingest/` contiene la adaptación biomédica. `setup.sh`
  Step 3b (copiaba i18n/ -> .claude/) está COMENTADO.
- ⚠️ NUNCA correr `setup.sh` esperando que sincronice skills.

### Sección B del SKILL.md — aliases estrictos
- Reescrita: aliases = solo sinónimos estrictos, sin mínimo, HARD FAIL
  eliminado (secciones B, E, Constraints).
- VALIDADO en 2 ingests (#70 y #35): 0 colisiones de conceptos en ambos,
  merges limpios con conceptos existentes. Funciona.

## Flujo de trabajo

1. `.venv/bin/python scripts/next_paper.py` — qué paper toca
2. `/ingest "..."` en Claude Code (Opus, medium effort)
3. `./scripts/verify_paper.sh` — ESPERAR a 0🔴 (el bloque 4 🟡 no bloquea)
4. `./scripts/commit_paper.sh` — pide TÍTULO y CUERPO
   - Al pegar el cuerpo, RECORTAR el ruido de Claude Code
     (`✻ Crunched...`, `※ recap:...`).
REGLA DE ORO: nunca commitear con verify en 🔴. Un paper, verificado,
commiteado, y el siguiente. NO encadenar ingests sin verificar.

## BUG 2 — enums inválidos — CONFIRMADO SISTEMÁTICO (no esporádico)

Aparece en CADA ingest, no de vez en cuando. El verify lo caza siempre;
la corrección es manual. Quedan ~60 papers -> el autofix SÍ vale la pena,
pero NO se construye aún: con pocos datos se construiría mal.

PLAN: anotar cada caso aquí abajo en cada ingest. Tras ~6 ingests con
catálogo completo, montar un autofix SEMIAUTOMÁTICO (detecta enum inválido
-> propone el válido -> pide confirmación). NO mapeo ciego: la corrección
depende del contenido (ej. 'emerging' podía ir a 'mainstream' O a
'historical' — solo se supo abriendo las páginas).

Enums válidos:
- claims.status: proposed | weakly_supported | supported | challenged | deprecated
- concepts.maturity: stable | active | emerging | deprecated
- foundations.status: mainstream | historical

Registro de casos vistos (AÑADIR UNA LÍNEA POR CASO EN CADA INGEST):
- #70 Hamon: claims.status 'tentatively_supported' x3 -> weakly_supported
- #35 AHR host-pathogen: foundations.status 'emerging' x2 -> mainstream

## Deuda pendiente (ordenada por prioridad)

1. AUTOFIX BUG 2 — ver sección de arriba. Montar tras ~6 ingests con
   catálogo. Con 60 papers por delante, se amortiza claramente.

2. LIMPIEZA DE ALIASES VIEJOS — estrategia REACTIVA decidida: NO limpiar
   los ~247 conceptos viejos proactivamente (8h de trabajo monótono). El
   check de duplicados marca las colisiones cuando ocurren; se limpia el
   concepto viejo en ese momento, con el recuento de aliases como pista.

3. FORMATO DE CLAIMS [cnn] vs [slug] — el ingest a veces genera claims con
   etiqueta [slug] en vez de [cnn] (pasó en #70). Decisión de diseño
   abierta: ¿migrar todo a [slug] (mejor, auto-documentado) o mantener
   [cnn]? Requiere tocar SKILL + validate_step4e.py + todos los papers.
   Sesión propia.

4. verify_paper.sh ELIGE EL PAPER POR FECHA DE MODIFICACIÓN — frágil: un
   ingest que toca papers viejos por edges le cambia el mtime y el verify
   valida el paper equivocado (pasó en #70 y #35, inofensivo las dos veces
   pero confuso). Considerar pasarle el slug del paper recién ingestado.

5. AUDITORÍA SEMÁNTICA REAL — sigue sin hacerse. Leer claims contra el PDF
   en ~5 papers y medir tasa de error de atribución. El check NO cubre esto.

6. foundations: 350+ — más foundations que conceptos. La sección C del
   SKILL crea una foundation por método. Revisar si sobre-crea.

7. i18n/en/skills/ingest/ obsoleto — marcar o congelar.

## Catálogo de bugs heredado (sigue vigente)

- Bug 3 — foundations con esquema inventado (type/category en vez de
  domain/status). Corregir a mano.
- Bug 6 — linter xref-asymmetry: checks de concepts/people/ideas
  (lint.py L313/325/355) sin parchear.

## Primeras acciones sugeridas para la próxima sesión

1. `git pull` && `git log --oneline -5` && `git status` — confirmar estado.
2. `./scripts/verify_paper.sh` — confirmar 0🔴.
3. Continuar ingestando (flujo de arriba), anotando cada caso de Bug 2.
   O, si ya hay ~6 ingests con catálogo, montar el autofix (deuda 1).

## Actualización en sesión — ingests #35 y #36

Registro Bug 2 (enums) — casos nuevos:
- #35 AHR host-pathogen: foundations.status 'emerging' x2 -> mainstream
- #36 macrophages-immunotherapy: SIN Bug 2 (caso negativo — el Bug 2 es
  frecuente pero NO universal)

Patrón nuevo detectado — fallos de ENLAZADO (familia distinta del Bug 2):
- #36 dejó un wikilink [[topics/]] VACÍO (Bug 5) y un reverse-link de claim
  multi-fuente sin escribir (claim trem2-tam-hcc-better-pd1-response apuntaba
  al paper #70 pero el #70 no le devolvía el enlace — §9.3 del audit).
- Junto con la Mejora 6 heredada: el ingest es fiable con el CONTENIDO pero
  descuidado con reverse-links y wikilinks. Si se repite en próximos ingests,
  candidato a revisión del SKILL o a un check dedicado. Seguir anotando.

Bloque 4 del verify — falsos positivos PERMANENTES conocidos (ignorar siempre):
1. claims Novae breast/colon (ratio 0.95) — dos benchmarks reales, convergencia.
2. conceptos immune-checkpoint-blockade vs innate-immune-checkpoint-blockade —
   vecinos legítimos (ICB adaptativo de células T vs checkpoints innatos
   mieloides CD47/SIRPA/LILRB). Confirmado por definiciones. NO fusionar.

El recuento de aliases en el bloque 4 funcionó en su primer uso real (#36):
identificó immune-checkpoint-blockade (13 aliases, viejo) vs el nuevo (2).

## Actualización — ingests #37 y #38

Registro Bug 2 (enums):
- #37 spatial-joint-profiling: SIN Bug 2 — ingest limpio, cero correcciones.
- #38 sympathetic-eosinophil: Bug 2 — foundations.status 'emerging' ->
  'mainstream' (foundation repeated-high-platform-stress-rhs).

Patrón Bug 2 a 5 ingests: 3 de 5 lo traen (#35,#38 sí / #36,#37 no).
'emerging' en foundations.status es el caso RECURRENTE (#35 y #38).
Será la primera regla del futuro autofix.

HALLAZGO DE DISEÑO (del #38) — para la sesión de revisión, NO para hoy:
(a) El enum foundations.status {mainstream|historical} NO tiene categoría
    para "establecido pero reciente". RHS es un paradigma que debuta en
    Tian 2026; 'emerging' era semánticamente correcto pero inválido.
    Corregido a 'mainstream', que miente un poco. Considerar añadir un
    valor al enum en vez de (o además de) montar el autofix.
(b) repeated-high-platform-stress-rhs se creó como FOUNDATION pero es
    metodología de UN solo paper. Ejemplo concreto para la deuda 6
    (foundations: 350+, ¿la sección C del SKILL sobre-crea?). Revisar
    qué fracción de las 350+ foundations son metodología de un paper.

Estado: 41 papers, 277 conceptos, 774 claims. Todo commiteado y pusheado.

## BUG nuevo — next_paper.py empareja mal por slug

Síntoma: tras commitear el #38, next_paper.py lo re-ofrece como SIGUIENTE
(no lo reconoce como YA EN WIKI).
Causa: next_paper.py genera el slug a partir del NOMBRE DEL PDF; /ingest
generó el slug del .md a partir del TÍTULO REAL del paper. No coinciden:
  PDF:  "A sympathetic-eosinophil axis ... stressto exacerbate ..."
  .md:  sympathetic-eosinophil-axis-orchestrates-psychological-stress.md
El "a-" inicial y el truncado hacen que no casen -> next_paper cree que
está pendiente.
Impacto: afecta a CUALQUIER paper cuyo nombre de archivo difiera del
título. Va a reincidir.
Workaround mientras no se arregle: ignorar el "SIGUIENTE PAPER" cuando
sea un paper ya commiteado; coger el primer PENDIENTE real de la lista.
Arreglo de fondo (sesión de tooling): que next_paper.py compare por algo
estable — DOI, o el slug oficial de research_wiki.py sobre el TÍTULO, no
sobre el nombre de archivo. Hermano de la deuda 4 (verify elige por mtime).

## Cierre de sesión 2026-05-28

Ingests del día: #35, #36, #37, #38, #39 (+ #70 cerrado al inicio).
Wiki: 42 papers, 279 conceptos, 784 claims. Todo commiteado y pusheado.

Registro Bug 2 actualizado:
- #39 hif-mitochondrial-bmdm: SIN Bug 2 — ingest limpio, cero correcciones.
- Recuento a 6 ingests: Bug 2 en 3 (#35, #38; los dos 'emerging' en
  foundations). #36, #37, #39 limpios. NO universal, pero frecuente.

Pendiente para próximas sesiones de TOOLING (no de ingest):
1. Bug next_paper.py — empareja por slug del nombre de PDF, no del título.
   Re-ofrece papers ya ingestados (#38). Arreglar de raíz: comparar por
   DOI o slug del título. Workaround actual: ignorar el "SIGUIENTE" si es
   un paper ya commiteado, coger el siguiente PENDIENTE real a mano.
2. Autofix Bug 2 — ya hay catálogo (3 casos, 'emerging' en foundations
   recurrente). Valorar si la solución es un autofix o ampliar el enum
   foundations.status con un valor para "establecido pero reciente".
3. Deuda 6 — foundations: 350+, la sección C del SKILL crea foundations
   de metodología de un solo paper (ej. RHS del #38). Revisar.
4. Auditoría semántica — SIGUE SIN HACERSE. La red que falta: el verify
   no comprueba si los claims dicen la verdad del paper. 5 papers, claims
   contra PDF, medir tasa de error de atribución.

Primeras acciones próxima sesión:
1. git pull && git log --oneline -5 && git status
2. ./scripts/verify_paper.sh -> 0🔴
3. Decidir: seguir ingestando, o dedicar la sesión a tooling (puntos 1-2).

## Parche — next_paper.py / #38
Añadida entrada a KNOWN_ALIASES para el #38 (sympathetic-eosinophil): el
slug del PDF no resolvía al del .md. Ya no se re-ofrece.
Nota: a 8 papers, KNOWN_ALIASES ha hecho falta 1 vez real (la del NF-κB fue
una decisión deliberada de una sesión inicial). Tasa baja -> el arreglo de
raíz de next_paper.py baja de prioridad; la lista manual es sostenible.

## Ingest #40 (NiCo) — caso nuevo de fallo de enlazado

El #40 creó un EDGE paper-a-paper (similar_method_to, confidence low)
hacia 'papers/cluster-shape-analysis-spatial' — un paper que NiCo cita
pero que NO está ingestado en el wiki. También escribió su wikilink en
## Related. Los dos eliminados.

Viola cross-references.md: los edges paper-a-paper son SOLO entre papers
existentes en wiki/papers/. El ingest no verificó que el destino existe.

Patrón de enlazado a 3 casos: #36 ([[topics/]] vacío + reverse-link a
medias), #40 (edge+wikilink a paper externo). El ingest es fiable con el
CONTENIDO pero NO verifica que los destinos de sus enlaces existan.
-> Mejora de SKILL para la sesión de tooling: instrucción explícita de
   "antes de escribir un edge o wikilink paper-a-paper, verificar que el
   destino existe en wiki/papers/".

Nota: research_wiki.py NO tiene 'remove-edge'. Borrar un edge concreto
requiere editar edges.jsonl a mano. Candidato a añadir a la herramienta.

Registro Bug 2: #40 SIN enum inválido. A 7 ingests: Bug 2 en 3 (#35,#38).

## Ingest #42 (skin atlas) — verificación post-descanso

- #42 ingestado ANTES de pasar por verify correctamente: el verify_paper.sh
  validó el #37 (bug del mtime, deuda 4), NO el #42. Verificado a posteriori
  apuntando validate_step4e.py directamente al #42: PASS, 30 claims, lint
  global 0🔴 0🟡. Limpio. Sin Bug 2.
- DEUDA 4 SUBE DE PRIORIDAD: el bug del mtime no es solo "confuso" — hizo que
  un 'RESULTADO: TODO OK' NO correspondiera al paper recién ingestado. Riesgo
  real de commitear sin verificar. Arreglo: pasar el slug explícito a
  verify_paper.sh. De los primeros en la sesión de tooling.
- relevance_tier 'emerging' en las 4 people nuevas: VÁLIDO (no es Bug 2). El
  SKILL L237 lo define como tier por defecto. Wiki: 144 emerging / 2 core.
- Pero: el lint NO valida a fondo enums de people (Bug 6, lint.py
  L313/325/355). El 0🟡 sobre las people fue correcto por suerte, no por
  verificación. Si el ingest pusiera un valor inválido en people, pasaría.
- RECORDATORIO de diseño (SKILL L245/285): el ingest NO auto-actualiza
  relevance_tier; emite 'PEOPLE TIER CHANGE SUGGESTED'. Revisar el output de
  cada /ingest por si hay que promover algún autor a 'core' a mano.

## Sesión de tooling — Deuda 4 (bug del mtime) RESUELTA

verify_paper.sh: acepta un slug opcional como $1.
  - Con slug: verifica ESE paper. Comprueba que el .md existe (error claro si no).
  - Sin slug: modo fecha (ls -t) como antes, PERO ahora imprime un [AVISO]
    visible de que puede no ser el paper recién ingestado.
commit_paper.sh: antes de la verificación, deduce el paper nuevo (.md con
  estado ?? o A en wiki/papers/). Si hay exactamente 1, le pasa el slug a
  verify_paper.sh. Si hay 0 o >1, cae a modo fecha (y el verify avisa).

Probado: verify con slug bueno / slug malo / sin argumento — OK. Lógica de
deducción de commit_paper.sh aislada (cuenta 0 y 1) — OK. Cableado con git
limpio (cae a modo fecha) — OK.
PENDIENTE DE PROBAR EN VIVO: el caso "1 paper nuevo deducido y slug pasado"
dentro de commit_paper.sh. Comprobar en el PRÓXIMO ingest real: la salida
debe decir ">>> Paper detectado para verificar: <slug>" y el verify debe
mostrar "[slug explícito]", NO "[AVISO] modo fecha".

Caso no cubierto (aceptado): un ingest que crea 2+ papers a la vez -> no se
puede deducir -> modo fecha + aviso. Raro; no se diseñó para ello.

Deuda menor nueva: validate_step4e.py peta con traceback crudo ante un
argumento inválido — debería dar un error legible. Baja prioridad.

## Sesión de tooling — fallos de enlazado paper-a-paper (SKILL.md)

Diagnóstico: la regla "el paper destino debe existir en wiki/papers/" estaba
EXPLÍCITA para citaciones (cross-references.md L53/L93) pero AUSENTE en la
viñeta de edges semánticos del Step 5 (SKILL.md L257). El #40 cayó por esa
rendija: cumplió el "clear cue" pero creó un edge hacia un paper no ingestado.
Arreglo: reescrita la viñeta del edge semántico — ahora exige (a) clear cue
Y (b) que el paper destino exista como archivo. Cubre el edge Y su wikilink
[[papers/]] en Related. Redactado como "file-existence check, not graph audit"
para no chocar con cross-references.md L99 (prohíbe auditorías de grafo en ingest).

LÍMITE: es una instrucción, no una barrera dura — sube la probabilidad, no
garantiza. La barrera dura sería un check. El lint YA caza el edge colgante
(dangling-edge 🟡, cazó el del #40). PENDIENTE de verificar: ¿caza también el
wikilink [[papers/]] huérfano, o solo el edge en edges.jsonl? Si no lo caza,
candidato a mejora de lint.py — sesión de código.

## Bug 2 (enums inválidos) — DECISIÓN: no se hace autofix

Inventario de enums hecho hoy (grep sobre todo el wiki):
- foundations.status: 424 mainstream, 2 historical — todos válidos.
- claims.status: supported/weakly_supported/proposed/challenged — todos válidos.
- concepts.maturity: active/emerging/stable + 1 'mainstream' (INVÁLIDO) -> corregido.
- people.relevance_tier: emerging/core — todos válidos.

Resultado: 1 solo enum inválido vivo en ~1700 entidades. Las correcciones
manuales de cada ingest (#70, #35, #38...) ya habían limpiado el resto.

DECISIÓN CONSCIENTE: no se construye autofix. Razón: el método actual
(lint caza el 🔴 -> corregir a mano -> commit) caza el 100% y el wiki está
limpio. Un autofix sería código de mantenimiento perpetuo para ahorrar
~3 min/ingest. No sale a cuenta. No reabrir sin un dato nuevo que cambie esto.

CLEANING PERIÓDICO en su lugar: cada cierto tiempo (p.ej. cada 10 papers),
correr el inventario de enums y corregir lo que aparezca inválido:
  grep -rh "^status:" wiki/foundations/*.md | sort | uniq -c
  grep -rh "^status:" wiki/claims/*.md | sort | uniq -c
  grep -rh "^maturity:" wiki/concepts/*.md | sort | uniq -c
  grep -rh "^relevance_tier:" wiki/people/*.md | sort | uniq -c
Valores válidos: foundations.status {mainstream,historical};
claims.status {proposed,weakly_supported,supported,challenged,deprecated};
concepts.maturity {stable,active,emerging,deprecated}.

PENDIENTE DE DISEÑO (sesión futura, NO urgente): foundations.status está
desequilibrado (424 mainstream / 2 historical). El modelo intentó meter
'emerging' 2 veces (#35,#38) porque quería decir "establecido pero reciente"
y el enum no tiene esa casilla. Valorar si añadir un valor al enum
foundations.status. Eso elimina la causa raíz del 'emerging' recurrente.
Tocar enum = tocar validador + lint.py + documentar. Su propia sesión.

## Ingest #45 — fallo de enlazado en UBICACIÓN NUEVA

El #45 metió un wikilink [[marekova-2024-endometrium-macrophage]] hacia un
paper no ingestado, DENTRO DEL CUERPO DE UN CLAIM (prosa). El propio ingest
escribió "(not yet ingested)" al lado y aun así puso los corchetes.
Importante: la mejora del SKILL de hoy cubría edges paper-a-paper y wikilinks
en ## Related — NO cubría wikilinks dentro del cuerpo de un claim. El fallo
de enlazado tiene más superficie de la que pensábamos.
-> Para la sesión de tooling: la regla "no enlazar a papers no ingestados"
   debería aplicar a CUALQUIER ubicación (claims, conceptos, prosa), no solo
   edges y Related. Y refuerza el caso del check dedicado: el lint SÍ cazó
   este (broken-link 🟡) — el check es la red fiable, el SKILL es probabilístico.

## Ingest #46 — BUG NUEVO: conceptos sin campo 'tags'

El #46 creó 8 conceptos, los 8 SIN el campo 'tags' (requerido) -> 8 🔴 de
lint [missing-field]. No es Bug 2 ni enlazado: es el ingest omitiendo un
campo obligatorio del frontmatter de concepts. Corregido a mano (set base
cachexia/oncology + tag de matiz por concepto).
Primera vez que se ve. Si reaparece en próximos ingests -> patrón, y
candidato a mejora del SKILL (Step de creación de conceptos) o a que el
ingest no omita campos requeridos. Vigilar en los próximos papers.

## Bug 6 (xref-asymmetry) — RESUELTO PARCIAL (rama people→paper)

El #50 (DECODE) disparó 3🟡 xref-asymmetry: el paper enlaza [[tianyi-zhao]] etc.
y las personas SÍ enlazaban de vuelta, pero con [[papers/decode-...]] (con
prefijo). El lint (lint.py L325) buscaba [[decode-...]] sin prefijo -> falso
positivo. Las páginas de people estaban bien; el bug era del lint.
Arreglo: L325 ahora acepta [[slug]], [[slug|...]], [[papers/slug]] y
[[papers/slug|...]]. Probado con no-regresión (link roto a propósito -> el lint
SÍ lo caza; restaurado -> 0🟡). No se tocó ninguna página de datos.

PENDIENTE (mismo bug de prefijo, probable, NO confirmado aún): las ramas de
concepts (~L313) e ideas (~L355) usan el mismo patrón `[[{slug}]] not in`
sin normalizar prefijo. Cuando aparezca un caso real, arreglar igual —idealmente
con un helper normaliza_wikilink() usado por las 4 ramas. NO se hizo hoy para
no refactorizar el corazón del linter a ciegas (riesgo de falsos negativos).

Nota sobre el ingest: es inconsistente con los prefijos — escribe [[slug]] sin
prefijo en el paper pero [[papers/slug]] con prefijo en la persona. El lint
ahora es robusto a ambos, pero podría unificarse el SKILL en el futuro.

## Sesión de vuelta de vacaciones — ingests #48,#50,#51,#52 + tooling

Ingests (todos limpios salvo lo indicado):
- VHL mitochondrial (Li 2026 Cell Metab) — limpio.
- DECODE (Zhao 2026 Nat Methods) — disparó falso positivo de lint (ver abajo).
- DHPS monocyte→TR-macrophage (Carrizo 2026 Nature) — limpio.
- single-cell cytokine dictionary (Oesinghaus 2025 bioRxiv) — limpio.
Wiki: 53 papers, 1012 claims, 344 conceptos.

Bug 6 (xref-asymmetry) — RESUELTO PARCIAL:
- Arreglada la rama people→paper en lint.py (~L325): ahora acepta el
  reverse-link con o sin prefijo papers/. Probado con no-regresión.
- PENDIENTE: mismo bug de prefijo probable en ramas concepts/ideas.
- PENDIENTE: relevance_tier NO se valida por lint (otro agujero del Bug 6).
  Valores válidos: emerging / established / core. Vigilar a mano.

Tiers de people (regla SKILL L242-244): >=10 core, >=4 established, resto
emerging. Los 'core' actuales (Ballestar, Calafell) son manual_override, no
por volumen. Ginhoux promovido a 'established' (primer established del wiki,
cruzó 4 papers). El ingest SUGIERE el cambio de tier, NO lo aplica — hay que
hacerlo a mano cuando aparezca "PEOPLE TIER CHANGE SUGGESTED".

Bug del 'tags' (#46): NO ha reaparecido en #48/#50/#51/#52. Caso aislado por
ahora, no patrón.

DECISIÓN — quitar el "(paper #N)" de los títulos de commit:
El #N viene del orden de next_paper.py, que NO es estable (cambia al añadir
papers o recalcular ranking). Meterlo en el mensaje de commit (permanente) es
poner un dato frágil que puede desincronizarse. Los identificadores estables
son slug + DOI + PMID, que ya van en el cuerpo del commit. A partir de ahora
los títulos van SIN "#N": "ingest: Autor AÑO Venue — título". (Esto también
elimina la fuente de los deslices de paréntesis en #43/#50/#52.)
Los 3 títulos viejos con #N o paréntesis sueltos NO se reescriben (están
pusheados; no vale un push --force por cosmética).

## Continuación sesión — ingests #53, #54

#53 skin fibroblast atlas (Steele 2025 Nat Immunol) — limpio. 21 claims,
taxonomía F1–F8, subtipos cross-tissue. Edge same_problem_as → #42 (Restrepo
skin atlas, que lo cita). Material directo para Project_Skin. Follow-ups
sugeridos: Buechler 2021, Korsunsky 2022, consensus dermal fibroblast atlas.

#54 AlphaCell "world model" (Chuai/He/Liu 2026 bioRxiv) — ML para biología,
zona nueva del wiki. Salió 0🔴 estructural pero NECESITÓ revisión semántica:
- c14 (HVG mal planteado para zero-shot) y c15 (embeddings discretos impiden
  zero-shot) estaban como status:supported / confidence 0.7-0.75, pero son
  ARGUMENTO DE AUTOR (críticas a STATE para justificar su arquitectura), no
  hallazgos. Recalibrados a status:proposed / confidence:0.5.
- Lección: los papers fuera del núcleo (macrófagos/hipoxia/skin) salen "chill"
  en el verify pero exigen MÁS lupa semántica, no menos. El verify da verde a
  un claim sobre-vendido igual que a uno sobrio.

## HALLAZGOS DE DISEÑO (del #54) — para sesión de tooling

1. El `type` de los claims (mechanistic/methodological/correlational/
   quantitative) NO es un campo estructurado del frontmatter. Vive SOLO inline
   en el bullet del paper (`papers/X.md`, línea "— type: Y —"). No se puede
   consultar, filtrar ni validar por type. El SKILL pide tipar (L172-175, L317)
   pero ese tipo no llega a ningún campo. Hermano del agujero de relevance_tier.
   DECISIÓN PENDIENTE: ¿hacer `type` un campo real del frontmatter del claim?
   (Permitiría queries tipo "claims mechanistic challenged", hoy imposible.)
2. El bullet inline del paper y el frontmatter del claim NO se sincronizan.
   Al recalibrar c14/c15 cambiamos el frontmatter (fuente de verdad) pero el
   bullet del paper sigue diciendo lo viejo. Desconexión de diseño.
3. CUARTO desliz de título de commit tecleado a mano (#43, #50, #52, #54).
   El #54 salió "Chuai,. et al He, Liu et al bioRxiv 2026, ...". Quitar el #N
   NO resolvió el problema: teclear autores+venue a mano no escala.
   PRIORIDAD SUBIDA: commit_paper.sh debe AUTOGENERAR el título desde el
   frontmatter del paper (autor/año/venue/título ya están ahí, limpios) y que
   el usuario solo confirme/edite. Títulos viejos NO se reescriben (pusheados).

## Estado al cierre de la sesión
55 papers, 1052 claims, 357 conceptos, 2341 edges. Todo commiteado y pusheado
(HEAD c15eb56). Árbol limpio.
Bug 6: rama people→paper resuelta; PENDIENTE concepts/ideas + validación de
relevance_tier y (nuevo) de claim type/status si se estructura.

## #55 effector-host interactome (IBD/T3SS) — INGESTADO, SIN COMMITEAR

Estado: ingestado, 7🔴 de tags YA CORREGIDOS (lint 0🔴 0🟡), pero SIN COMMITEAR.
Pendiente para mañana (cabeza fresca):
1. Revisión SEMÁNTICA de los 23 claims — zona fuera del núcleo (microbiología).
   Mirar con lupa los claims que ligan efectores bacterianos a enfermedad:
   t3ss-effectors-enriched-crohns-depleted-uc,
   cd-prevalent-effectors-target-cd-susceptibility-proteins,
   effector-prevalence-crohns-vs-uc-divergence, y los de "modulación inmune".
   ¿Correlación metagenómica (lo que da un mapa de interactoma) o causalidad
   sobre-vendida? Recalibrar status/confidence como en c14/c15 del #54 si hace falta.
2. Revisar edges paper-a-paper (grep en edges.jsonl).
3. commit_paper.sh — TÍTULO A MANO CON CUIDADO (ya van 4 deslices), o mejor aún
   esperar a tener el autogenerado.
Los tags arreglados están en disco sin commitear; el commit los recogerá.

## BUG DEL 'tags' — AHORA ES PATRÓN, no caso aislado
Reapareció en #55 (7 conceptos sin tags) tras 5 papers limpios. Junto con el #46
(8 conceptos sin tags), el patrón es claro: el ingest omite 'tags' en papers
que crean MUCHOS conceptos de golpe (lotes grandes), fuera del núcleo.
-> Sesión de tooling: arreglar en el SKILL (Step de creación de conceptos debe
   exigir tags) o añadir autofix. Ya no es aceptable parchear a mano cada vez.

## CORRECCIÓN — #55 YA COMMITEADO (anula la entrada "SIN COMMITEAR" de arriba)
El #55 (Young, Dohai, Halder et al., Nat Microbiol 2026, effector-host
interactome T3SS) está COMMITEADO Y PUSHEADO (HEAD 54ba110). La entrada previa
que lo daba por "sin commitear / pendiente revisión" queda ANULADA:
- Revisión semántica de los 23 claims: HECHA. Resultado: el ingest los calibró
  bien (factuales en quantitative/high; los de enfermedad Crohn/UC en
  correlational/medium sin verbos causales; los funcionales NF-κB/citoquinas en
  pharmacological/medium con validación experimental real). Los dos dudosos
  (c13 sequence-independence, c22 COG6/TNIP1↔Crohn) ya estaban amortiguados
  (c22 en confidence:low). DECISIÓN: no tocar nada. A diferencia del #54, aquí
  no había miscalibración.
- Edges paper-a-paper: ninguno (zona nueva del wiki, sin con qué conectar).
- Título salió limpio (rompió la racha de 4 deslices).

## ESTADO REAL AL CIERRE
56 papers, 1075 claims, 364 conceptos, ~2387 edges. Todo commiteado y pusheado
(HEAD 54ba110). Árbol limpio.

## TAREA DE MANTENIMIENTO DEL PROPIO HANDOFF (pendiente)
Este handoff ha crecido por acumulación cronológica durante la sesión. Antes de
que crezca más en sesiones futuras, conviene CONSOLIDARLO en secciones estables:
Estado actual / Deuda pendiente priorizada / Decisiones de diseño / Bugs
catalogados. Y archivar lo que ya es historia. No urgente, pero un handoff que
solo crece acaba siendo tan difícil de navegar como no tenerlo.
