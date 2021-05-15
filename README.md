# WDFtoTXT
Batch convert wdf files to txt for Raman spectroscopy analysis

This script is a wrapper around the wdf-export util from renishawWiRE creared by alchem0x2A

Required: Python 3.6 or above, pip3

# Setup
All commands are assumed to be ran in the project's root directory.

Optional: Do configuration in a virtual environment

	python3 -m venv ENVIR_NAME

	cd ENVIR_NAME/bin

	. ./activate



To install dependencies, run the following command.

	pip3 install requirements.txt


If running into issues with wheels, run the following commands instead.

	pip3 install cython pybind11

	pip3 install --no-binary :all: --no-use-pep517 numpy

	pip3 install renishawWiRE



If you want to run wdftotxt from anywhere in your system, you can do one of the following:

NOTE: Be careful when doing these

	1. Move wdftotxt to a directory in your PATH (recommended: /usr/local/bin, atleast on mac)

	2. Add the directory of wdftotxt to your PATH

	3. (If using a virtual environment) Copy wdftotxt to your environment's bin folder

		cp wdftotxt ENVIR_NAME/bin/wdftotxt


# Usage

	wdftotxt [OPTION]... [FILE]...

Batch converts .wdf files to .txt format, then stores all files in a single output directory

Wrapper around wdf-export utility from renishawWiRE

Arguments:

        -h

show this help message and exit

        -f

filters out files that do not end in .wdf

        -o DIR

changes the output directory to DIR

        -r

recursively convert files of any input directories

Examples:



	wdftotxt *

Converts all files in the current directory to txt format



	wdftotxt -f *

Converts only files ending in .wdf 



	wdftotxt -o outdir *

Sets the output directory to outdir



	wdftotxt -r *

Recursively enters any directories and converts files within them

	
