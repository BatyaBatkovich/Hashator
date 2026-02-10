#!/usr/bin/env python3
import argparse
from typing import Iterable

ASCII_BANNER = r"""
 _   _           _           _
| | | |         | |         | |
| |_| | __ _ ___| |__   __ _| |_ ___  _ __
|  _  |/ _` / __| '_ \ / _` | __/ _ \| '__|
| | | | (_| \__ \ | | | (_| | || (_) | |
\_| |_/\__,_|___/_| |_|\__,_|\__\___/|_|
""".strip(
    "\n"
)

def format_list(items: Iterable[str]) -> str:
    items = list(items)
    if not items:
        return "(none)"
    return "\n".join(f"- {item}" for item in items)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hashator",
        description="Generate a hash image and display available algorithms.",
        epilog=(
            "Quick help:\n"
            "  - List algorithms:    hashator --list-algos\n"
            "  - Generate image:     hashator -d test.png\n"
            "  - Type of hash:       hashator -t\n"
            "  - Choose file:        hashator -f fr_dict.txt\n"
            "  - Complete example:   hashator -t sha256 -d test.png -f fr_dict.txt\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--list-algos",
        action="store_true",
        help="Display the list of available algorithms.",
    )
    parser.add_argument(
        "-d",
        "--dest",
        help="Name of the output PNG file (test.png).",
    )
    parser.add_argument(
        "-t",
        "--hash-algo",
        help="Choose the type of hash algorithm (sha224, sha256, etc).",
    )
    parser.add_argument(
        "-f",
        "--file",
        default="fr_dict.txt",
        help="Input file to hash (default: fr_dict.txt).",
    )
    return parser