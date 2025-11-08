#!/usr/bin/env bash
# ------------------------------------------------------------
# Mission:AI Possible - Markdown Sanitizer for Open WebUI Prompts
# macOS-safe version (no mapfile, compatible with Bash 3.2)
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
files_list=""
while IFS= read -r f; do
  count=$((count+1))
  echo " $count) $f"
  eval "file_$count='$f'"
done < <(find . -type f -name "*.md" | sort)

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
  sed $'s/\xC2\xA0/ /g' | \
  sed $'s/\xE2\x80\x8B//g' | \
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
