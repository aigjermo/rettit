"""Rettit is a small utility for making corrections to specific datasets"""

from sys import argv
from .console import Console


def main(args):
    """Run whichever action the user selected"""

    console = Console(args)
    infile = console.input()
    outfile = console.output()
    action = console.action_type()

    if action == "precipitation":
        # This is how it would look more or less, infile and outfile are file
        # pointers ready for reading/writing
        #
        #   outfile.write(precipitation.rett_it(infile, <params>))
        pass

    if action == "noop":
        # quick line by line passthrough to demonstrate piping data etc.
        for line in infile:
            outfile.write(line)


if __name__ == "__main__":
    main(argv[1:])
