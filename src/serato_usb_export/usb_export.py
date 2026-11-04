import re
from importlib.metadata import version, PackageNotFoundError

import requests

from serato_tools.usb_export import main as original_main


def _parse_version(v: str) -> tuple[int, ...]:
    """Numeric release parts only, e.g. "5.2.0" -> (5, 2, 0); "5.3.0rc1" -> (5, 3, 0)."""
    parts = []
    for part in v.split("."):
        digits = re.match(r"\d+", part)
        if not digits:
            break
        parts.append(int(digits.group()))
    return tuple(parts)


def check_latest_version(package_name: str) -> None:
    """Warn (never exit) if the installed package is behind PyPI. Silently skips if offline."""
    try:
        installed_version = version(package_name)
    except PackageNotFoundError:
        return

    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=5)
        response.raise_for_status()
        latest_version = response.json()["info"]["version"]
    except (requests.RequestException, ValueError, KeyError):
        return  # offline or PyPI unavailable; the export doesn't need the network

    if _parse_version(installed_version) < _parse_version(latest_version):
        print(f"WARNING: {package_name} is outdated (installed: {installed_version}, latest: {latest_version}).")
        print(f'run "pip install --upgrade {package_name}"\n')


def main():
    check_latest_version("serato-tools")
    original_main()


if __name__ == "__main__":
    main()
