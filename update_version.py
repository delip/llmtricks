"""
This script automatically updates the version in llmtricks/_version.py using the version in pyproject.toml
"""

import re
import pathlib
import subprocess
import tomli  # You'll need to add this to your build dependencies


def git_check_uncommitted_changes():
    try:
        return "\n".join(
            [
                x
                for x in subprocess.check_output(["git", "status", "--porcelain"])
                .decode("utf-8")
                .strip()
                .split("\n")
                if "_version.py" not in x
            ]
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
    automatically update in llmtricks/_version.py using the version in pyproject.toml
    """
    changes = git_check_uncommitted_changes()
    if changes:
        print("WARNING: You have uncommitted changes!!")
        print(changes)
        return -1

    pyproject_path = pathlib.Path("pyproject.toml")
    version_path = pathlib.Path("llmtricks/_version.py")

    with open(pyproject_path, "rb") as f:
        pyproject_data = tomli.load(f)
        version = pyproject_data["project"]["version"]

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
