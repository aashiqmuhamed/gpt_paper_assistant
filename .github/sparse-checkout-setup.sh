#!/bin/bash
# Run this once locally to exclude the papers/ archive from your working directory.
# Papers will still exist on GitHub, just won't download when you pull.
git sparse-checkout init --no-cone
git sparse-checkout set '/*' '!papers/'
echo "Done. papers/ directory will no longer be downloaded on pull."
echo "You can still browse papers at: https://github.com/<owner>/<repo>/tree/main/papers"
