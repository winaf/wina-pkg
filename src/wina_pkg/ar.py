import platform
from typing import List


def default_ar_cmd() -> str:
    return "lib.exe" if platform.system().lower() == "windows" else "ar"


def build_command(ar_cmd: str, output: str, objects: List[str]) -> List[str]:
    if platform.system().lower() == "windows":
        return [ar_cmd, f"/OUT:{output}", *objects]

    return [ar_cmd, "rcs", output, *objects]
