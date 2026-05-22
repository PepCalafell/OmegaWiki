#!/usr/bin/env bash
# verify_paper.sh — verificación post-ingest de OmegaWiki
# Uso: ./scripts/verify_paper.sh
# Corre validator + lint + check de formato + estado del wiki sobre el
# paper más reciente. NO toca git. Pensado para correr tras cada /ingest.

set -u
cd "$(dirname "$0")/.." || { echo "ERROR: no se pudo ir a la raíz del repo"; exit 1; }

PY=".venv/bin/python"
[ -x "$PY" ] || PY="python3"   # fallback si no hay venv

FAIL=0

echo "========================================================"
echo " VERIFICACIÓN POST-INGEST"
echo "========================================================"

# --- Paper más reciente ---
NEW_PAPER=$(ls -t wiki/papers/*.md 2>/dev/null | head -1)
if [ -z "$NEW_PAPER" ]; then
  echo "ERROR: no se encontró ningún paper en wiki/papers/"
  exit 1
fi
echo "Paper más reciente: $(basename "$NEW_PAPER")"
echo ""

# --- 1. Validator Step 4E ---
echo "--- 1. Validator (validate_step4e) ---"
VAL_OUT=$("$PY" tools/validate_step4e.py "$NEW_PAPER" 2>&1)
echo "$VAL_OUT" | head -3
if echo "$VAL_OUT" | grep -q "PASS"; then
  echo "  -> validator OK"
else
  echo "  -> validator FALLÓ"
  FAIL=1
fi
echo ""

# --- 2. Lint completo ---
echo "--- 2. Lint ---"
LINT_OUT=$("$PY" tools/lint.py --wiki-dir wiki/ 2>&1 | head -1)
echo "  $LINT_OUT"
# extraer recuento de 🔴 y 🟡
RED=$(echo "$LINT_OUT" | grep -oE '[0-9]+ 🔴' | grep -oE '[0-9]+' || echo "?")
YEL=$(echo "$LINT_OUT" | grep -oE '[0-9]+ 🟡' | grep -oE '[0-9]+' || echo "?")
if [ "$RED" = "0" ] && [ "$YEL" = "0" ]; then
  echo "  -> lint limpio (0 🔴, 0 🟡)"
else
  echo "  -> lint con avisos: $RED 🔴, $YEL 🟡  (revisar antes de commitear)"
  [ "$RED" != "0" ] && FAIL=1   # 🔴 es bloqueante; 🟡 solo aviso
fi
echo ""

# --- 3. Formato source_papers en los 3 claims más recientes ---
echo "--- 3. Formato source_papers (debe ser multilínea) ---"
INLINE_FOUND=0
for c in $(ls -t wiki/claims/*.md 2>/dev/null | head -3); do
  LINE=$(grep -m1 "source_papers" "$c")
  echo "  $(basename "$c"): $LINE"
  # formato malo = corchete inline en la misma línea
  if echo "$LINE" | grep -qE 'source_papers:\s*\['; then
    INLINE_FOUND=1
  fi
done
if [ "$INLINE_FOUND" = "1" ]; then
  echo "  -> AVISO: formato inline detectado — normalizar antes de commitear"
  FAIL=1
else
  echo "  -> formato multilínea OK"
fi
echo ""

# --- 4. Estado del wiki ---
echo "--- 4. Estado del wiki ---"
echo "  papers:  $(ls wiki/papers/*.md 2>/dev/null | wc -l)"
echo "  claims:  $(ls wiki/claims/*.md 2>/dev/null | wc -l)"
echo "  concepts:$(ls wiki/concepts/*.md 2>/dev/null | wc -l)"
echo "  edges:   $(wc -l < wiki/graph/edges.jsonl 2>/dev/null || echo '?')"
echo ""

echo "========================================================"
if [ "$FAIL" = "0" ]; then
  echo " RESULTADO: TODO OK — listo para commit_paper.sh"
else
  echo " RESULTADO: HAY PROBLEMAS — revisar antes de commitear"
fi
echo "========================================================"
exit $FAIL
