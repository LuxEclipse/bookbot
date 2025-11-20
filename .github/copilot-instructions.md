<!-- Copilot / AI Agent instructions for the BookBot repository -->
# BookBot — Copilot instructions

This repository is intentionally small and minimal. These instructions give an AI coding agent the essential, discoverable knowledge needed to be productive here.

- **Repo entrypoint:** `main.py` — currently a tiny script that prints a greeting.
- **Docs:** `README.md` at the repo root explains the project intent (Boot.dev learning project).

Keep changes minimal and explicit. This project is a learning sandbox — prefer clarity over cleverness.

What to do first
- Read `main.py` and `README.md` to confirm intent before changing behavior.
- If you add features, include a one-line description in `README.md` and keep `main.py` as the CLI entrypoint unless adding a new package layout.

Running and quick checks
- Run the program locally with: `python3 main.py`.
- There are currently no tests, virtualenv, or dependency files. Do not add heavy infra unless the user asks.

Code and style patterns to follow (project-specific)
- Single-file entry: The repository currently uses a single script (`main.py`). If you introduce modules, put them under a top-level package directory (e.g., `bookbot/`) and keep `main.py` as a thin runner.
- Minimal dependencies: Avoid adding external packages without explicit user approval. If you must add dependencies, include a `requirements.txt` and update `README.md` with install/run instructions.
- Keep prints and I/O explicit and simple — this project is used for learning/demo, not production.

Recommended change workflow for PRs
- Small, focused commits with clear messages (e.g., `Add CLI args to main.py`).
- If you add code that needs verification, include a short manual test step in the PR description (e.g., `Run: python3 main.py --foo`).

Files and places to reference when editing
- `main.py` — current runtime entrypoint and simplest place to reproduce behavior.
- `README.md` — update with new usage or features.

What not to do
- Don't scaffold heavy CI, testing frameworks, or packaging unless requested; this repository is intentionally minimal.
- Don't change the repository layout drastically without asking the user.

If you need clarification
- Ask the user which direction they want (expand to a package, add testing, or keep minimal). Provide a short plan and requested files to change.

Contact points in the repo
- Root `README.md` — reflects project intent and should be kept in sync with changes.

Examples (small tasks)
- Add a CLI flag: modify `main.py` to parse `sys.argv` and document usage in `README.md`.
- Add a module: create a `bookbot/` package and import from `main.py`; update `README.md` with the new command to run.

Keep instructions concise in PR bodies and reference this file when giving AI agents new tasks.
