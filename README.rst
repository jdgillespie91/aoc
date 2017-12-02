aoc
===

*Requires Python 3.6*

My solutions to `Advent of Code 2017`__.

.. _aoc: https://adventofcode.com

__ aoc_

Installation
------------

From a wheel,

.. code-block:: bash

    $ pip install /path/to/wheel

From source,

.. code-block:: bash

    $ git clone
    $ cd aoc && pip install -e .

Usage
-----

To see the results for day one for example, use

.. code-block:: bash

    $ aoc -d 1 -f data/day1.txt

For more detailed help instructions, see

.. code-block:: bash

    $ aoc --help

Share
-----

To share, package the repository and share the resulting wheel in `dist/`.

.. code-block:: bash

    $ python setup.py bdist_wheel
