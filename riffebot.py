#!/usr/bin/env python3

import sys
import platform
import argparse
import requests

# Check for python3
if sys.version_info[0] != 3:
    sys.stderr.write("This must be ran with python 3")
    sys.stderr.write("Version: {0}\n".format(platform.python_version()))
    sys.exit(1)

def main(args):
    """

    """

if __name__ == "__main__":
    main(args)