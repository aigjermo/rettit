"""Rettit is a small utility for making corrections to specific datasets"""

from .console import Console

CONSOLE = Console()

if CONSOLE.action() == 'hello':
    print "Hello world"
