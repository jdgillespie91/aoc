Day Two
=======

Task
----

Given a two-dimensional array, the task_ is to perform one of two operations across the rows and sum the results of
these operations.

In the first part of the puzzle, the operation is the difference between the largest element of the row and the
smallest.

In the second part of the puzzle, the operation is the quotient given when dividing the only pair of numbers that
divide to give an integer value.

.. _task: https://adventofcode.com/2017/day/2

Implementation
--------------

Part One
~~~~~~~~

We need the difference between the largest and smallest elements in each row.

.. code-block:: python

    >>> rows = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    >>> def find_difference(row):
    ...     return max(row) - min(row)

We do this across the rows with

.. code-block:: python

    >>> differences = map(find_difference, rows)

Finally, sum the results with

.. code-block:: python

    >>> print(sum(differences))
    18

Part Two
~~~~~~~~
