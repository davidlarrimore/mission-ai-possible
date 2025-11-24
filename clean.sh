#!/bin/sh
# ------------------------------------------------------------
# Mission:AI Possible - Markdown Sanitizer for Open WebUI Prompts
# POSIX-friendly (no Bash-only features; works when run via sh)
# ------------------------------------------------------------
# Scans recursively for .md files, lets you pick one,
# cleans problem characters and replaces content in place
# (creates .bak backup automatically)
# ------------------------------------------------------------

set -e

echo "🧠 Mission:AI Possible — Markdown Sanitizer"
echo "------------------------------------------"
echo "Searching recursively for Markdown files..."

# Build a numbered list of .md files
count=0
FILES_TMP=$(mktemp)
find . -type f -name "*.md" -print | sort > "$FILES_TMP"

while IFS= read -r f; do
  count=$((count+1))
  echo " $count) $f"
  eval "file_$count='$f'"
done < "$FILES_TMP"

rm -f "$FILES_TMP"

if [ "$count" -eq 0 ]; then
  echo "❌ No Markdown files found."
  exit 1
fi

echo ""
printf "Select the file number you want to sanitize: "
read choice

# Validate numeric input
if ! echo "$choice" | grep -Eq '^[0-9]+$'; then
  echo "❌ Invalid selection. Must be a number."
  exit 1
fi

eval FILE="\$file_$choice"
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "❌ Invalid file number."
  exit 1
fi

BACKUP="${FILE}.bak"
TMPFILE=$(mktemp)
NBSP_CHAR=$(printf '\302\240')
ZWSP_CHAR=$(printf '\342\200\213')

echo ""
echo "⚠️  Backing up file to: $BACKUP"
cp "$FILE" "$BACKUP"

echo "🧼 Cleaning and normalizing '$FILE' ..."
echo ""

# 1. Convert smart punctuation → ASCII
# 2. Replace triple backticks with ```
# 3. Strip NBSP and zero-width spaces
# 4. Normalize line endings
iconv -f utf-8 -t utf-8 -c "$FILE" | \
  sed 's/“/"/g; s/”/"/g; s/‘/'"'"'/g; s/’/'"'"'/g; s/—/--/g; s/–/-/g; s/•/-/g' | \
  sed -E 's/```+([[:space:]]*)/```/g' | \
  sed "s/${NBSP_CHAR}/ /g" | \
  sed "s/${ZWSP_CHAR}//g" | \
  awk '{sub(/\r$/,""); print}' > "$TMPFILE"

mv "$TMPFILE" "$FILE"

ENCODING=$(file -I "$FILE" | awk -F'=' '{print $2}')

echo ""
echo "✅ Sanitization complete!"
echo "File updated in place: $FILE"
echo "Backup saved as: $BACKUP"
echo "Encoding verified as: $ENCODING"
echo ""
echo "Summary of fixes:"
echo " - Smart quotes → straight quotes"
echo " - Em/en dashes → -- or -"
echo " - Bullets → -"
echo " - Triple backticks (```) → ```"
echo " - Non-breaking & zero-width spaces removed"
echo ""
echo "✅ Ready for Open WebUI."
