"""
This script automatically updates the version in llmtricks/_version.py using the version in pyproject.toml
"""

import re
import pathlib


def update_version():
    """
    automatically update in llmtricks/_version.py using the version in setup.py
    """
    setup_path = pathlib.Path("setup.py")
    version_path = pathlib.Path("llmtricks/_version.py")

    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()
        version_match = re.search(r'version\s*=\s*"([^"]+)"', content)
        if not version_match:
            raise ValueError("Could not find version in setup.py")
        version = version_match.group(1)

    # Update version in _version.py
    with open(version_path, "w", encoding="utf-8") as f:
        f.write(f'__version__ = "{version}"\n')

    print(f"Updated version in {version_path} to {version}")


if __name__ == "__main__":
    update_version()
