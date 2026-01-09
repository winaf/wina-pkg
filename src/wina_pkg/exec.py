import subprocess
import sys
from typing import List

from .log import debug


def run_command(cmd: List[str], dry_run: bool) -> None:
    if dry_run:
        print(" ".join(cmd))
        return

    debug("Ejecutando:")
    debug(" ".join(cmd))

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        debug("💥 Error durante el empaquetado")
        sys.exit(e.returncode)
