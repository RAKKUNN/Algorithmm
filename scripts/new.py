#!/usr/bin/env python3
"""
Usage:
  python scripts/new.py <platform> <id> "<title>" <url>
    [--lang {python,cpp,go}] [--tags TAGS] [--time TIME] [--space SPACE] [--status STATUS] [--date YYYY-MM-DD]

Example:
  python scripts/new.py leet 1 "Two Sum" https://leetcode.com/problems/two-sum --lang python --tags "array,hash-table"
"""

import argparse
from pathlib import Path
from datetime import datetime
import re
import sys

def slugify(title: str) -> str:
    slug = re.sub(r'[^A-Za-z0-9가-힣]+', '-', title.strip())
    return slug.strip('-').lower()

def main():
    parser = argparse.ArgumentParser(description="Create a new problem from templates.")
    parser.add_argument("platform")
    parser.add_argument("id")
    parser.add_argument("title")
    parser.add_argument("url")
    parser.add_argument("--lang", choices=["python", "cpp", "go"], default="python")
    parser.add_argument("--tags", default="")
    parser.add_argument("--time", default="?")
    parser.add_argument("--space", default="?")
    parser.add_argument("--status", default="draft")
    parser.add_argument("--date", default=None)
    args = parser.parse_args()

    # map language to folder & extension
    lang_dir_map = {"python": "py", "cpp": "cpp", "go": "go"}
    ext_map      = {"python": "py", "cpp": "cpp", "go": "go"}

    lang_dir = lang_dir_map[args.lang]
    ext      = ext_map[args.lang]

    slug = slugify(args.title)
    prob_dirname = f"{args.id}-{slug}"
    sol_dir = Path("solutions") / lang_dir / args.platform / prob_dirname
    sol_dir.mkdir(parents=True, exist_ok=True)

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")

    tpl_path = Path("templates") / lang_dir / f"main.{ext}"
    if not tpl_path.exists():
        print(f"[ERROR] Template not found: {tpl_path}", file=sys.stderr)
        sys.exit(1)

    # ✅ Force UTF-8 when reading template
    tpl = tpl_path.read_text(encoding="utf-8")

    # fill placeholders
    filled = (
        tpl.replace("{platform}", args.platform)
           .replace("{id}", args.id)
           .replace("{title}", args.title)
           .replace("{url}", args.url)
           .replace("{tags}", args.tags)
           .replace("{date}", date_str)
           .replace("{time}", args.time)
           .replace("{space}", args.space)
           .replace("{status}", args.status)
    )

    main_file = sol_dir / f"main.{ext}"
    # ✅ Force UTF-8 when writing solution
    main_file.write_text(filled, encoding="utf-8")

    (sol_dir / "README.md").write_text("", encoding="utf-8")
    (sol_dir / "cases.txt").write_text("", encoding="utf-8")

    print(f"[OK] Created: {sol_dir}")

if __name__ == "__main__":
    main()
