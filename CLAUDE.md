# serato-usb-export

Thin PyPI wrapper that exposes `serato_tools.usb_export.main` as the `serato_usb_export` command. All real logic lives in [serato-tools](https://github.com/bvandrc/serato-tools); bug fixes and features belong there, not here.

## Layout

- `src/serato_usb_export/usb_export.py` — re-exports `main` from serato-tools. Keep it that way.
- `pyproject.toml` — package version and the `serato_tools>=X` dependency floor.
- `CHANGELOG.md` — user-visible changes per version, written as `pypi-publishing.md` says.
- `README.md` — user-facing install/usage/arguments. The Arguments section mirrors serato-tools' argparse options; check `serato_usb_export --help` after a serato-tools bump and update it.

## Conventions

The repo's conventions live in `conventions/` and are imported here in full. They apply to all work in this repo, and everything else here extends them.

@conventions/all.md
@conventions/python.md
@conventions/pypi-publishing.md

`conventions/` is synced from `bvandrc/bvandrc-conventions` by `.github/workflows/sync-conventions.yml`, which deletes and recreates the directory on every run, so edits made here are lost: change them upstream. When a sync adds a new file to `conventions/`, add a matching `@conventions/<file>` import here.

- Python 3.12+ (matches serato-tools).

## Updating serato-tools

1. Raise `serato_tools>=` in `pyproject.toml`, bump `version`, and add a `CHANGELOG.md` entry.
2. Install into a clean venv and diff `serato_usb_export --help` against the README's Arguments section.
3. Merge, then release as `pypi-publishing.md` says. PyPI's trusted publisher names `release.yml` and its `pypi` environment, so renaming either means updating it on PyPI too.

## Checks (same as CI, `.github/workflows/lint.yml`)

Install the tools with `pip install -e ".[dev]"`.

```bash
serato_usb_export --help   # smoke test: CLI starts against installed serato-tools
pyright
ruff check .
ruff format --check .
```
