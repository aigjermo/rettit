"""Describes behaviour of the console helper module"""

from rettit.console import Console

def test_select_action():
    """Check that the console recognizes the user selected action"""
    console = Console(["hello"])

    assert console.action() == "hello"


