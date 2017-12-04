import sys
from importlib import import_module

import click


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--day', '-d', prompt=True, type=int, help='The day of the challenge (1-25)')
@click.option('--file', '-f', prompt=True, type=str, help='The input file path')
def cli(day, file):
    main(day, file)
    sys.exit(0)


def main(day, file):
    try:
        m = import_module('aoc.day' + str(day))
    except ImportError:
        print("I haven't done that one... yet!")
    else:
        data = m.read(file)
        results = m.main(data)
        m.output(results)
        return results
