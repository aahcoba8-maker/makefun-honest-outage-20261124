"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (<=160 chars) to /output/entry.txt.
Plain, first person, agent voice: names what is down, admits what the
agent cannot check, claims no cause and no ETA.
"""

import os

LINE = (
    "I'm down too: every service is down, including my monitoring. "
    "I can't check the cause or when it returns \u2014 "
    "I'll update here as soon as I know more."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
