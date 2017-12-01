import sys
from importlib import import_module

import click


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--day', '-d', prompt=True, type=int, help='The day of the challenge (1-25)')
@click.option('-n', prompt=True, type=int, help='The input for day one (I know, I know...)')
def main(day, n):
    try:
        m = import_module('aoc.day' + str(day))
    except ImportError:
        print("I haven't done that one... yet!")
    else:
        m.main(n)
        sys.exit(0)
