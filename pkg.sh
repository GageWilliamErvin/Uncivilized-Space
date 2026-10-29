#!/usr/bin/env bash

# Output markdown file
OUTPUT="out.md"

# Clear or create the output file at the start
> "$OUTPUT"

# Enable nullglob so the loop doesn't run if no .json files exist
shopt -s nullglob

# Loop through all JSON files in the current working directory
for file in jsons/*.json; do
    # Skip if out.md itself matches (just in case)
    [ "$file" = "$OUTPUT" ] && continue

    # Append header and content to out.md
    echo "# $file" >> "$OUTPUT"
    echo '```json' >> "$OUTPUT"
    cat "$file" >> "$OUTPUT"
    echo '```' >> "$OUTPUT"
    echo "" >> "$OUTPUT" # Adds a blank line between entries for readability
done

echo "Successfully combined JSON files into $OUTPUT"