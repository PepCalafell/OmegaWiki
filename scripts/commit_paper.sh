#!/usr/bin/env bash
# commit_paper.sh — commit + push de un ingest de OmegaWiki
# Uso:
#   ./scripts/commit_paper.sh                -> pide TÍTULO y luego CUERPO (pegado)
#   ./scripts/commit_paper.sh mensaje.txt    -> usa el archivo entero como mensaje
#
# SALVAGUARDA: re-corre verify_paper.sh antes de commitear. Si hay 🔴 o el
# validator falla, ABORTA. Nunca commitea un wiki roto ni con mensaje vacío.

set -u
cd "$(dirname "$0")/.." || { echo "ERROR: no se pudo ir a la raíz del repo"; exit 1; }

# --- 1. Verificación previa (salvaguarda) ---
# Deducir el paper recién ingestado: el .md nuevo (?? o A) en wiki/papers/.
# Si hay exactamente uno, se le pasa el slug a verify_paper.sh para que
# valide ESE paper (y no "el más reciente por fecha", que puede ser otro
# si el ingest tocó papers viejos por edges). Si hay 0 o >1, no se adivina:
# verify_paper.sh cae a su modo fecha (y avisa por sí mismo).
mapfile -t NEW_PAPERS < <(git status --porcelain wiki/papers/ \
  | grep -E '^(\?\?|A ) ' | grep -E '\.md$' | sed -E 's/^.{3}//')
VERIFY_SLUG=""
if [ "${#NEW_PAPERS[@]}" -eq 1 ]; then
  VERIFY_SLUG=$(basename "${NEW_PAPERS[0]}" .md)
  echo ">>> Paper detectado para verificar: $VERIFY_SLUG"
elif [ "${#NEW_PAPERS[@]}" -gt 1 ]; then
  echo ">>> AVISO: ${#NEW_PAPERS[@]} papers nuevos detectados — no se puede"
  echo "    deducir cuál verificar. verify_paper.sh usará el modo fecha."
fi
echo ">>> Corriendo verificación previa..."
if ! ./scripts/verify_paper.sh $VERIFY_SLUG; then
  echo ""
  echo "ABORTADO: la verificación falló. Arregla los problemas y reintenta."
  exit 1
fi
echo ""

# --- 2. ¿Hay algo que commitear? ---
if [ -z "$(git status --porcelain wiki/)" ]; then
  echo "ABORTADO: no hay cambios en wiki/ para commitear."
  exit 1
fi

echo ">>> Cambios que se van a commitear:"
git status --short wiki/
echo ""

# --- 3. Mensaje de commit ---
MSG_FILE=$(mktemp)
CLEANUP=1

if [ $# -ge 1 ]; then
  # mensaje desde archivo: se usa entero, tal cual
  if [ ! -f "$1" ]; then
    echo "ERROR: el archivo de mensaje '$1' no existe."
    rm -f "$MSG_FILE"
    exit 1
  fi
  cp "$1" "$MSG_FILE"
  echo ">>> Usando mensaje de: $1"
else
  # modo interactivo: TÍTULO aparte + CUERPO pegado
  echo "========================================================"
  echo " TÍTULO del commit (una línea)"
  echo " Convención: 'ingest: Autor AÑO Venue — título corto'"
  echo "========================================================"
  read -r -p ">>> Título: " TITULO
  if [ -z "$(echo "$TITULO" | tr -d '[:space:]')" ]; then
    echo "ABORTADO: el título está vacío."
    rm -f "$MSG_FILE"
    exit 1
  fi

  echo ""
  echo "========================================================"
  echo " CUERPO del commit"
  echo " Pega el resumen del /ingest. Cuando termines: ENTER y"
  echo " luego Ctrl+D en una línea vacía."
  echo "========================================================"
  CUERPO_FILE=$(mktemp)
  cat > "$CUERPO_FILE"

  # ensamblar: título + línea en blanco + cuerpo
  {
    echo "$TITULO"
    echo ""
    cat "$CUERPO_FILE"
  } > "$MSG_FILE"
  rm -f "$CUERPO_FILE"

  echo ""
  echo "--------------------------------------------------------"
  echo ">>> Mensaje de commit completo:"
  echo "--------------------------------------------------------"
  cat "$MSG_FILE"
  echo "--------------------------------------------------------"
fi

# --- 4. Validar que el mensaje no está vacío ---
MSG_CONTENT=$(grep -v '^#' "$MSG_FILE" | grep -v '^[[:space:]]*$')
if [ -z "$MSG_CONTENT" ]; then
  echo "ABORTADO: el mensaje de commit está vacío."
  rm -f "$MSG_FILE"
  exit 1
fi

# --- 4b. Confirmación antes de commitear ---
if [ $# -eq 0 ]; then
  echo ""
  read -r -p ">>> ¿Commitear con este mensaje? [s/N] " RESP
  case "$RESP" in
    s|S|si|Si|SI|y|Y) ;;
    *) echo "ABORTADO por el usuario."; rm -f "$MSG_FILE"; exit 1 ;;
  esac
fi

# --- 5. Commit + push ---
echo ""
echo ">>> Commiteando..."
git add wiki/
git commit -F "$MSG_FILE" || { echo "ERROR en git commit"; rm -f "$MSG_FILE"; exit 1; }

echo ""
echo ">>> Pusheando a origin..."
git push origin "$(git branch --show-current)" || { echo "ERROR en git push — el commit está hecho localmente"; rm -f "$MSG_FILE"; exit 1; }

rm -f "$MSG_FILE"
echo ""
echo "========================================================"
echo " COMMIT + PUSH OK"
git log --oneline -1
echo "========================================================"
