#!/usr/bin/env python

import argparse
import mom6_parameter_scanner


def parseCommandLine():
    """
    Parse the command line positional and optional arguments.
    This is the highest level procedure invoked from the very end of the script.
    """
    global debug  # Declared global in order to set it

    # Arguments
    parser = argparse.ArgumentParser(
        description="""
      MOM6param_scan.py scans MOM_parameter_doc files and summarizes configurations.
      It can also parse input.nml and logfiles for Fortran namelists.
      """,
        epilog="Written by A.Adcroft, 2015.",
    )
    parser.add_argument(
        "files", type=str, nargs="+", help="""parameter-files/tar-files to scan."""
    )
    parser.add_argument(
        "-nml", "--namelist", action="store_true", help="scan for Fortran namelists."
    )
    parser.add_argument(
        "-mnml",
        "--mom6namelist",
        action="store_true",
        help="scan for Fortran namelists ignoring logfile.000000.out.",
    )
    parser.add_argument(
        "-log",
        "--log",
        action="store_true",
        help="scan for model output in FMS log file.",
    )
    parser.add_argument(
        "-if",
        "--ignore_files",
        action="append",
        default=[],
        help="file patterns to ignore when searching.",
    )
    parser.add_argument(
        "-m",
        "--assume_mom6",
        action="store_true",
        help="assume FILE is a MOM6 parameter file. By default only MOM_parameter_doc.{all,short} are scanned.",
    )
    parser.add_argument(
        "-x", "--exclude", action="append", default=[], help="parameters to exclude."
    )
    parser.add_argument(
        "-fmt",
        "--format",
        choices=["json", "table", "html", "text"],
        default="json",
        help="output format.",
    )
    parser.add_argument(
        "-t", "--transpose", action="store_true", help="transpose html table."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="turn on debugging information."
    )
    args = parser.parse_args()

    debug = args.debug

    return args


# Invoke parseCommandLine(), the top-level prodedure
if __name__ == "__main__":
    args = parseCommandLine()
    mom6_parameter_scanner.main(args)
