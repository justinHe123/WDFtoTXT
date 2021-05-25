#!/usr/bin/env python3.6
from renishawWiRE import WDFReader
from argparse import ArgumentParser
from pathlib import Path
import re
import sys

def main():
    usage_msg = """%(prog)s - convert a wdf file to txt
    %(prog)s [OPTION]... [FILE]

    Extracts and formats data from a wdf file into multiple txt file.
    All txt files will be placed into a single directory.

    """
    # Parse arguments
    parser = ArgumentParser(usage=usage_msg)
    parser.add_argument('file')
    parser.add_argument("-o", "--output",
        help="set OUTPUT as the output directory")
    parser.add_argument("-b", "--base",
        help="set BASE as the base name for output files")
    parser.add_argument("-p", "--parent",
        help="set PARENT as the parent directory of the output directory")
    parser.add_argument("--no-duplicate",
        action="store_true",
        help="if specified, causes program to exit if output directory already exists")
    parser.add_argument("--keep-path",
        action="store_true",
        help="if specified, will not strip leading directories when creating output directory")
    args = parser.parse_args()

    ### Further argument parsing ###
    # Strip any leading directories from path
    dir_split = args.file.split('/')
    no_dir = dir_split[-1]
    # Strip any trailing extension from file
    stripped = no_dir.split('.')[0]

    # Set base name to stripped file name, if not specified
    if args.base is None:
        args.base = stripped

    # Set to output directory to stripped file name + "_txt", if not specified
    # If keep_path specified, will not strip leading directories
    if args.keep_path:
        dir_split[-1] = ''
        stripped = '/'.join(dir_split) + stripped
    if args.output is None:
        args.output = stripped + "_txt"

    # If parent directory specified, make sure to append '/' for proper traversal
    # Otherwise, leave blank as to not disrupt relative/absolute pathing
    if args.parent is None:
        args.parent = ''
    else:
        args.parent += '/'

    dirname = f'{args.parent}{args.output}'

    try:
        if not Path(args.file).is_file():
            # Error: invalid input file
            raise Exception(f'invalid input file: {args.file}')

        # Initialize reader
        try:
            reader = WDFReader(args.file)
        except Exception as e:
            # Error: cannot read file
            raise Exception(f'cannot read file: {args.file}')

        # Create output directory
        directory = Path(dirname)
        if directory.exists() and not directory.is_dir():
            # Error: existing path is a file
            raise Exception(f'output directory is already a file: {dirname}')
        if directory.exists() and args.no_duplicate:
            # Error: duplicate directory
            raise Exception(f'directory already exists: {dirname}')

        directory.mkdir(parents=True, exist_ok=not args.no_duplicate)

        # Parse reader
        spectra_length = len(reader.spectra)
        row, col = 0, 0
        spectra = reader.spectra.flatten()
        start = 0
        # Order of iteration:
        # iterate x and y simultaneously
        # iterate xdata and spectra simultaneously
        # spectra[i][j] where i increments ++, and j increments when i = len
        for i in range(reader.capacity):
            x = reader.xpos[i]
            y = reader.ypos[i]      
            # Create file and write line by line
            filename = f'{dirname}/{args.base}__X_{x.round(4)}__Y_{y.round(4)}.txt'
            with open(filename, 'w') as file:
                for j in range(reader.point_per_spectrum):
                    # Format: wavenumber    spectra value
                    file.write(f'{reader.xdata[j]}\t{spectra[start + j]}\n')
            start += reader.point_per_spectrum
        exit(0)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)