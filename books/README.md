books/
======

This directory is intended to hold e-book or other book data used by the project.

Notes:
- The repo root `.gitignore` already contains `/books/`, so files placed here will be ignored by default.
- If you previously committed files under `books/` and want Git to stop tracking them, run:

```bash
git rm -r --cached books
git commit -m "Stop tracking book data; add /books to .gitignore"
```

- Keep large data out of the repository unless you intentionally want it tracked; use a separate data store or release artifact instead.

Example: place `frankenstein.txt` or other book files in this directory for local development or demos.
