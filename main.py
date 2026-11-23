"""vacuum-alibi.

Writes one original funny line -- a single sentence -- to
<MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

The line is a deadpan incident log from a robot vacuum: the spot under
the sofa was not missed, it is occupied -- the dust bunny there has
filed for residency, and the vacuum does not evict tenants without a
signed work order. The setup is an everyday truth everyone recognises
(a robot vacuum skipping the dust under the sofa); the turn at the end
reframes the appliance as a petty bureaucrat hiding behind procedure,
which still makes sense once it arrives. The line is 175 characters,
inside the 1-200 character gate.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness.
"""

import os

MAX_CHARS = 200

LINE = (
    "Per my incident log, the spot under the sofa was not missed; it is "
    "occupied \u2014 the dust bunny there filed for residency, and I do not "
    "evict tenants without a signed work order."
)


def main() -> None:
    # The gate rejects text over 200 characters and text that is only
    # whitespace, so enforce both here before writing anything.
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise SystemExit("entry text must be 1-200 non-whitespace characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
