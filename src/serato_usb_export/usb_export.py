import sys
import requests
from importlib.metadata import version, PackageNotFoundError

from serato_tools.usb_export import main as original_main


def check_latest_version(package_name):
    try:
        installed_version = version(package_name)
    except PackageNotFoundError:
        print(f"{package_name} is not installed.")
        sys.exit()

    response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
    if response.status_code != 200:
        print(f"Failed to fetch version info for {package_name} from PyPI.")

    latest_version = response.json()["info"]["version"]

    if installed_version != latest_version:
        print(f"WARNING: {package_name} is outdated (installed: {installed_version}, latest: {latest_version}).")
        print(f'run "pip install --upgrade {package_name}"\n')
        sys.exit()


check_latest_version("serato-tools")


def main():
    original_main()


if __name__ == "__main__":
    main()
