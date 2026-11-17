# serato-usb-export

Thin PyPI wrapper that exposes `serato_tools.usb_export.main` as the `serato_usb_export` command. All real logic lives in [serato-tools](https://github.com/bvandrc/serato-tools); bug fixes and features belong there, not here.

## Layout

- `src/serato_usb_export/usb_export.py` — re-exports `main` from serato-tools. Keep it that way.
- `pyproject.toml` — package version and the `serato_tools>=X` dependency floor.
- `CHANGELOG.md` — user-visible changes per version; a release's notes come from its section.
- `README.md` — user-facing install/usage/arguments. The Arguments section mirrors serato-tools' argparse options; check `serato_usb_export --help` after a serato-tools bump and update it.

## Conventions

- **No runtime version checks or network calls.** Users get a newer serato-tools when the maintainer raises the dependency floor and publishes a new release. Don't add warnings or PyPI checks at startup.
- Don't add dependencies the wrapper doesn't import directly.
- Python 3.12+ (matches serato-tools).

## Updating serato-tools

1. Raise `serato_tools>=` in `pyproject.toml`, bump `version`, and add a `CHANGELOG.md` entry.
2. Install into a clean venv and diff `serato_usb_export --help` against the README's Arguments section.
3. Merge, then publish a GitHub release tagged `v<version>` (e.g. `gh release create v1.3.0 --title v1.3.0 --notes ""`). Publishing it runs `.github/workflows/release.yml`, which fails before building if the tag isn't `v` + the version, uploads to PyPI through trusted publishing, fills empty release notes from the version's `CHANGELOG.md` section, and attaches the built distributions. PyPI's trusted publisher names that workflow file and its `pypi` environment, so renaming either means updating it on PyPI too.

## Checks (same as CI, `.github/workflows/lint.yml`)

Install the tools with `pip install -e ".[dev]"`. Format with `ruff check --fix .` then `ruff format .`.

```bash
serato_usb_export --help   # smoke test: CLI starts against installed serato-tools
pyright
ruff check .               # every rule except those pyproject.toml's [tool.ruff.lint] turns off, each with a reason
ruff format --check .
```

Ruff is pinned below its next minor version (`ruff>=0.17,<0.18` in the `dev` extra), since only a minor release adds stable rules or changes the formatting. Moving to a new minor version is its own PR, deciding for each new rule whether to fix what it flags or ignore it. For a one-off finding that's right as it is, silence it on its line with `# noqa: RULE` and a reason, rather than adding to the ignore list.
