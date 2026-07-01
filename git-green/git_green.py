#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="git-green: Maintain an organic, semantic Git contribution graph."
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # generate subcommand
    generate_parser = subparsers.add_parser(
        "generate", help="Generate organic contributions for a past date range"
    )
    generate_parser.add_argument(
        "--days", type=int, default=60, help="Number of past days to generate commits for"
    )

    # install subcommand
    subparsers.add_parser(
        "install", help="Install daily systemd timer autostart configuration"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    print(f"git-green: CLI initialized with command: '{args.command}'")

if __name__ == "__main__":
    main()
