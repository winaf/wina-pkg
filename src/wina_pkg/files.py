import os
import sys
from typing import Iterable, List, Set


def read_response_file(spec: str) -> List[str]:
    if spec == "@-":
        return [line.strip() for line in sys.stdin if line.strip()]

    path = spec[1:]
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def resolve_files(files: Iterable[str]) -> List[str]:
    resolved = []
    for f in files:
        if f.startswith("@"):
            resolved.extend(read_response_file(f))
        else:
            resolved.append(f)
    return resolved


def collect_from_dirs(dir: str, excludes: Set[str]) -> List[str]:
    objects = []
    for root, _, files in os.walk(dir):
        for name in files:
            if name.endswith(".o") and name not in excludes:
                objects.append(os.path.join(root, name))
    return objects
