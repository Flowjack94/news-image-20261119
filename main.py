#!/usr/bin/env python3
"""Publish the finished front page for the make.fun news-image bounty.

Copies the entry.png that sits next to this file into the output
directory named by MAKEFUN_OUTPUT_DIR (default /output). The file is
copied byte for byte, so the published image is exactly the checked
1024x1024 front page. Standard library only, no network, no
randomness: running it twice produces the same bytes in the same place.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(ENTRY, target)
    print("wrote %s" % target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
