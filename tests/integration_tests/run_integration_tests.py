# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
This script will run all the integration tests from this folder.
"""

from __future__ import print_function

import time
import sys
import os
import glob


import subprocess


def main():

    current_folder, current_file = os.path.split(__file__)

    # Ensures code coverage will be generated
    coverage_path = os.path.normpath(
        os.path.join(current_folder, "..", "python", "third_party", "coverage")
    )

    before = time.time()
    try:
        filenames = glob.iglob(os.path.join(current_folder, "*.py"))
        for filename in filenames:

            # Skip the launcher. :)
            if filename.endswith(current_file):
                continue

            print("=" * 79)
            print("Running %s" % os.path.basename(filename))
            print("=" * 79)

            if "--with-coverage" in sys.argv:
                args = [
                    sys.executable,
                    coverage_path,
                    "run",
                    "-a",
                    filename
                ]
            else:
                args = [
                    sys.executable,
                    filename
                ]

            subprocess.check_call(args)

            print()
            print()
    except Exception:
        print("=" * 79)
        print("Tests failed in %.2f" % (time.time() - before))
        raise
    else:
        print("=" * 79)
        print("Tests passed in %.2f" % (time.time() - before))


if __name__ == "__main__":
    main()
