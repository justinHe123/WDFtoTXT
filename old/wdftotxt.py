#!/usr/bin/env python3.6
from renishawWiRE import WDFReader
from argparse import ArgumentParser
import re
from pathlib import Path

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
    parser.add_argument("--no-duplicate",
        action="store_true",
        help="if specified, causes program to exit if output directory already exists")
    parser.add_argument("--keep-path",
        action="store_true",
        help="if specified, will not strip leading directories when creating output directory")
    args = parser.parse_args()

    ### Further argument parsing ###
    # Strip any trailing extensions from path name
    no_extension = args.file.split('.')[0]
    # Strip any leading directories from path
    no_directories = no_extension.split('/')[-1]

    # Set base name to stripped file name, if not specified
    if args.base is None:
        args.base = no_directories

    # Set to output directory to stripped file name + "_txt", if not specified
    # If keep_path specified, retains any leading directories
    if args.output is None:
        args.output = (no_extension if args.keep_path else no_directories) + "_wdfout"

    # Initialize reader
    reader = WDFReader(args.file)
    # Create output directory
    Path(args.output).mkdir(parents=True, exist_ok=not args.no_duplicate)

    # Parse reader
    spectra_length = len(reader.spectra)
    row, col = 0, 0
    # Order of iteration:
    # iterate x and y simultaneously
    # iterate xdata and spectra simultaneously
    # spectra[i][j] where i increments ++, and j increments when i = len
    for i in range(reader.capacity):
        x = reader.xpos[i]
        y = reader.ypos[i]      
        spectra = reader.spectra[row][col]
        # Create file and write line by line
        with open('{}/{}__X_{}__Y_{}).txt'.format(args.output, args.base, x.round(4), y.round(4)), 'w') as file:
            for j in reversed(range(reader.point_per_spectrum)):
                # Format: wavenumber    spectra value
                file.write('{}\t{}\n'.format(reader.xdata[j], spectra[j]))
        # Determine row, col from i  
        row += 1
        if row == spectra_length:
            row, col = 0, col + 1

# def convert_multi(file, base, out):
#     usage_msg = """%(prog)s - convert wdf files to txt
#     %(prog)s [OPTION]... [FILE]

#     Batch converts .wdf files to .txt format, then stores all files in a single output directory. 
#     Wrapper around wdf-export utility from renishawWiRE

#     """
#     # Parse arguments
#     parser = ArgumentParser(usage=usage_msg)
#     parser.add_argument('file')
#     parser.add_argument("-f", "--filter",
#         action="store_true",
#         help="filters out files that do not end in .wdf")
#     parser.add_argument("-o", "--out",
#         metavar="DIR",
#         help="changes the output directory to DIR")
#     parser.add_argument("-r", "--recursive",
#         action="store_true",
#         help="recursively convert files of any input directories")
#     args = parser.parse_args()

#     if args.out is None:



# # Converter class handles file parsing, file name formatting, and conversion
# class Converter:
#     def __init__(self, file, base, out):
#         self.reader = WDFReader(file)
#         self.base = base
#         self.out = out
#     def convert(self):
#         # Create diretory
#         Path(self.out).mkdir(parents=True)
#         # Parse reader
#         spectra_length = len(self.reader.spectra)
#         row, col = 0, 0
#         # Order of iteration:
#         # iterate x and y simultaneously
#         # iterate xdata and spectra simultaneously
#         # spectra[i][j] where i increments ++, and j increments when i = len
#         for i in range(self.reader.capacity):
#             x = self.reader.xpos[i]
#             y = self.reader.ypos[i]      
#             spectra = self.reader.spectra[row][col]
#             # Create file and write line by line
#             with open('{}/{}__X_{}__Y_{}).txt'.format(self.out, self.base, x.round(4), y.round(4)), 'w') as file:
#                 for j in reversed(range(self.reader.point_per_spectrum)):
#                     # Format: wavenumber    spectra value
#                     file.write('{}\t{}\n'.format(self.reader.xdata[j], self.spectra[j]))
#             # Determine row, col from i  
#             row += 1
#             if row == spectra_length:
#                 row, col = 0, col + 1


if __name__ == '__main__':
    main()