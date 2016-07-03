"""Module handling user interaction via command line"""

from argparse import ArgumentParser

class Console(object):
    """Console interface for rettit"""

    def __init__(self, params=None):
        """Parse parameters"""

        parser = ArgumentParser(description='Apply automatic correction to data sets')

        parser.add_argument('type', help='the type of data to correct')

        self.args = parser.parse_args(params)

    def action(self):
        """Get user specified action"""
        return self.args.type
