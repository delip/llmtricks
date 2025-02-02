"""
This script automatically updates the version in llmtricks/_version.py using the version in pyproject.toml
"""

import re
import pathlib
import subprocess


def git_check_uncommitted_changes():
    try:
        return (
            subprocess.check_output(["git", "status", "--porcelain"])
            .decode("utf-8")
            .strip()
        )
    except Exception as e:
        return ""


def get_git_commit_hash():
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode("utf-8")
            .strip()
        )
    except Exception as e:
        return "None"


def update_version():
    """
    automatically update in llmtricks/_version.py using the version in setup.py
    """
    changes = git_check_uncommitted_changes()
    if changes:
        print("WARNING: You have uncommitted changes!!")
        print(changes)
        return -1

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
        f.write(f'__git_commit_hash__ = "{get_git_commit_hash()}"\n')

    print(f"Updated version in {version_path} to {version}")
    print(f"Git commit hash: {get_git_commit_hash()}")
    return 0


if __name__ == "__main__":
    status = update_version()
    exit(status)
