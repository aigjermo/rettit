"""Describes behaviour of the console helper module"""

from sys import stdin, stdout
from nose.tools import assert_equals, assert_raises
from rettit.console import Console

def init_console(args):
    """Convenience function for creating a console for testing"""

    def raise_error(message):
        """Alternative error handler for argparse"""

        raise Exception(message)

    return Console(args, error_callback=raise_error)


def test_require_type_parameter():
    """Check that the console fails with missing data type"""

    with assert_raises(Exception):
        init_console([])


def test_validate_type_parameter():
    """Check that the console fails with incorrect data type"""

    with assert_raises(Exception):
        init_console(["hello"])


def test_type_precipitation():
    """Check that the console recognizes 'precipitation' as a valid type"""

    console = init_console(["precipitation"])

    assert_equals(console.action_type(), "precipitation")


def test_default_input_stdin():
    """Check that console input is stdin when not instructed otherwise"""

    console = init_console(["precipitation"])

    assert_equals(console.input(), stdin)


def test_default_output_stdout():
    """Check that console output is stdout when not instructed otherwise"""

    console = init_console(["precipitation"])

    assert_equals(console.output(), stdout)


def test_read_from_file_parameter():
    """Check that console input is file if -i is given"""

    console = init_console(["precipitation", "-i", "tst/input.dat"])

    infile = console.input()
    assert_equals(infile.name, "tst/input.dat")
    assert_equals(infile.mode, "r")


def test_write_to_file_parameter():
    """Check that console output is file if -o is given"""

    console = init_console(["precipitation", "-o", "tst/output.dat"])

    outfile = console.output()
    assert_equals(outfile.name, "tst/output.dat")
    assert_equals(outfile.mode, "w")

