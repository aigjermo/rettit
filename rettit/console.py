"""Module handling user interaction via command line"""

from sys import stdin, stdout
from argparse import ArgumentParser, FileType


class Console(object):
    """Console interface for rettit"""

    def __init__(self, params=None, error_callback=None):
        """Parse parameters"""

        parser = ArgumentParser(description="Apply automatic correction to data sets")

        # allow passing a callback to override the default error handler in testing
        if error_callback:
            parser.error = error_callback

        parser.add_argument("type",
                            choices=["precipitation", "noop"],
                            help="the type of data to correct")

        parser.add_argument("-i", "--input",
                            default=stdin,
                            type=FileType('r'),
                            help="read input data from file")

        parser.add_argument("-o", "--output",
                            default=stdout,
                            type=FileType('w'),
                            help="write output data to file")

        self.args = parser.parse_args(params)


    def action_type(self):
        """Get user specified action"""

        return self.args.type


    def input(self):
        """Get file pointer to data input"""

        return self.args.input


    def output(self):
        """Get file pointer to data output"""

        return self.args.output
