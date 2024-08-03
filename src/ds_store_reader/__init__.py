"""DS Store Reader - Apple DS_Store Reader."""

from __future__ import annotations

# MIT License
#
# Copyright (c) 2018 Sebastian Neef
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__title__ = "DS Store Reader"
__author__ = "Sebastian Neef"
__version__ = "1.0.0"
__license__ = "MIT License"


import os
import sys

from .dsstore import DSStore


def run() -> None:
    """Run CLI Interface."""
    program_name = sys.argv[0]
    if len(sys.argv) < 2:
        sys.exit(f"Usage: python {program_name} <DS_STORE FILE> [--debug]")
    if not os.path.exists(sys.argv[1]):
        sys.exit(f"File not found: Usage {program_name} <file> [--debug]")
    with open(sys.argv[1], "rb") as f:
        store = DSStore(f.read(), debug="--debug" in sys.argv[2:])
        files = store.traverse_root()
        print("File Count: ", len(files))
        print("\n".join(files))


if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    run()
