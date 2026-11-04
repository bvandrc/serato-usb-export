# serato-usb-export

Thin PyPI wrapper that exposes `serato_tools.usb_export.main` as the `serato_usb_export` command. All real logic lives in [serato-tools](https://github.com/bvandrc/serato-tools); bug fixes and features belong there, not here.

## Layout

- `src/serato_usb_export/usb_export.py` — re-exports `main` from serato-tools. Keep it that way.
- `pyproject.toml` — package version and the `serato_tools>=X` dependency floor.
- `README.md` — user-facing install/usage/arguments. The Arguments section mirrors serato-tools' argparse options; check `serato_usb_export --help` after a serato-tools bump and update it.

## Conventions

- **No runtime version checks or network calls.** Users get a newer serato-tools when the maintainer raises the dependency floor and publishes a new release. Don't add warnings or PyPI checks at startup.
- Don't add dependencies the wrapper doesn't import directly.
- Python 3.12+ (matches serato-tools).

## Updating serato-tools

1. Raise `serato_tools>=` in `pyproject.toml` and bump `version`.
2. Install into a clean venv and diff `serato_usb_export --help` against the README's Arguments section.
3. Publish via the manually triggered "Build & Publish" workflow.

## Checks (same as CI, `.github/workflows/lint.yml`)

```bash
serato_usb_export --help   # smoke test: CLI starts against installed serato-tools
pylint $(git ls-files '*.py')
pyright
black --check -l 120 .
```
