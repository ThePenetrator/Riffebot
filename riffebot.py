#!/usr/bin/env python3

import sys
import platform
import argparse
import requests
import sqlite3

# Check for python3
if sys.version_info[0] != 3:
    sys.stderr.write("This must be ran with python 3")
    sys.stderr.write("Version: {0}\n".format(platform.python_version()))
    sys.exit(1)

def main(args):
    """

    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Program to monitor Riffe Lake levels",
        epilog="Text following argument descriptons",
    )
    args_optional = parser._action_groups.pop()
    args_required = parser.add_argument_group("Required Settings")

    # Required args
    args_required.add_argument("-p", "--pole-rate", type=float, action='store', 
                                required=True)

    # Optional args
    args_optional.add_argument("-o", "--optional", action='store',
                                required=False)
    parser._action_groups.append(args_optional)
    args = parser.parse_args()