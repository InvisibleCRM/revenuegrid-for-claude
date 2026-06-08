#!/usr/bin/env python3
"""Require changed Claude plugins to bump their plugin.json version."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


BASE_REF = "main"
PLUGIN_MANIFEST = Path(".claude-plugin") / "plugin.json"


def run_git(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_stdout(args: list[str]) -> str:
    return run_git(args).stdout.strip()


def read_index_file(path: Path) -> str | None:
    result = run_git(["show", f":{path.as_posix()}"], check=False)
    if result.returncode != 0:
        return None
    return result.stdout


def read_base_file(path: Path) -> str | None:
    result = run_git(["show", f"{BASE_REF}:{path.as_posix()}"], check=False)
    if result.returncode != 0:
        return None
    return result.stdout


def parse_version(contents: str | None, path: Path, source: str) -> str | None:
    if contents is None:
        return None

    try:
        manifest = json.loads(contents)
    except json.JSONDecodeError as error:
        raise ValueError(f"{source} {path} is not valid JSON: {error}") from error

    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"{source} {path} must contain a non-empty string `version`")
    return version


def staged_files() -> list[Path]:
    output = git_stdout(["diff", "--cached", "--name-only", "--diff-filter=ACMRT"])
    return [Path(line) for line in output.splitlines() if line]


def plugin_dirs(root: Path) -> list[Path]:
    return sorted(
        manifest.parent.parent.relative_to(root)
        for manifest in root.rglob(PLUGIN_MANIFEST.as_posix())
        if ".git" not in manifest.parts
    )


def is_relative_to(path: Path, parent: Path) -> bool:
    if parent == Path("."):
        return True
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def changed_plugins(root: Path) -> list[Path]:
    files = staged_files()
    if not files:
        return []

    plugins = plugin_dirs(root)
    return [
        plugin
        for plugin in plugins
        if any(is_relative_to(staged_file, plugin) for staged_file in files)
    ]


def main() -> int:
    try:
        root = Path(git_stdout(["rev-parse", "--show-toplevel"]))
        run_git(["rev-parse", "--verify", "--quiet", BASE_REF])

        failures: list[str] = []
        for plugin in changed_plugins(root):
            manifest_path = plugin / PLUGIN_MANIFEST
            try:
                staged_version = parse_version(
                    read_index_file(manifest_path),
                    manifest_path,
                    "staged",
                )
                base_version = parse_version(
                    read_base_file(manifest_path),
                    manifest_path,
                    BASE_REF,
                )
            except ValueError as error:
                failures.append(str(error))
                continue

            if staged_version is None:
                failures.append(f"staged {manifest_path} is missing")
            elif base_version is not None and staged_version == base_version:
                failures.append(
                    f"{manifest_path} version must differ from {BASE_REF} "
                    f"for changed plugin {plugin}"
                )

        if failures:
            print("Plugin version check failed:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
            return 1

        return 0
    except subprocess.CalledProcessError as error:
        print(error.stderr.strip() or str(error), file=sys.stderr)
        return error.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
