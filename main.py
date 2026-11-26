"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum-placard line for an ordinary office object,
presented as an ancient artifact, to entry.txt.

Stdlib only. Deterministic: the placard is a fixed constant, no
randomness, no network, no reads from anywhere else.
"""

import os

PLACARD = (
    "Paperclip, c. 1962, bent steel. The empire's smallest shackle: "
    "it held departments together a century, then rusted in a drawer. "
    "Gift of a clerk who never left."
)


def resolve_output_path():
    """Resolve the output path, in priority order."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    text = PLACARD.strip()
    if not text:
        raise ValueError("placard must not be blank")
    if len(PLACARD) > 180:
        raise ValueError("placard must be at most 180 characters long")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PLACARD + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
