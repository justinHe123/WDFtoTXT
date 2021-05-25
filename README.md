# WDFtoTXT
Batch convert wdf files to txt for Raman spectroscopy analysis

This script is a wrapper around the wdf-export util from renishawWiRE by alchem0x2A

# Installation

Clone this repository, then change into the locally created directory for setup.

	git clone https://github.com/justinHe123/WDFtoTXT.git
	
	cd WDFtoTXT

# Setup
Required: Python 3.6 or above, pip3

All commands are assumed to be ran in the project's root directory.

Optional: Do configuration in a virtual environment

	python3 -m venv ENVIR_NAME

	cd ENVIR_NAME/bin

	. ./activate



To install the script, use pip.

	pip3 install .


If running into issues with wheels, run the following commands before running the command above..

	pip3 install cython pybind11

	pip3 install --no-binary :all: --no-use-pep517 numpy

# Usage

	wdftotxt [OPTION]... [FILE]...

Batch converts .wdf files to .txt format, then stores all files in a single output directory. Outp
ut files will retain the directory hierarchy of input files.


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

	
