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

For each row, we need to identify the quotient of the only pair of integers that divide to give an integer value.

To this end, we define a function that tells us whether a pair of integers divide to give an integer quotient and, if
so, the value of this quotient.

.. code-block:: python

    >>> def is_integer_quotient(pair):
    ...     q = pair[0] / pair[1]
    ...
    ...     if q == int(q):
    ...         return (True, q)
    ...
    ...     if 1/q == int(1/q):
    ...         return (True, 1/q)
    ...
    ...     return (False, 0)

Then we need to search all possible pairs of integers in our row for the one that divides to give an integer quotient.
Given that we are assuming only one such pair exists, we can stop when we find the first pair.

We generate all possible pairs with the following function. It is an extension of the cartesian product of the row,
discarding any pair where we have joined an element to itself.

.. code-block:: python

    >>> def generate_pairs(row):
    ...     count = 0
    ...     length = len(row)
    ...     all_pairs = product(row, row)
    ...
    ...     while count < length * length:
    ...         count += 1
    ...         pair = next(all_pairs)
    ...
    ...         if count % (length + 1) == 1:
    ...             continue
    ...
    ...         yield pair


We then search the pairs for the first that gives an integer quotient.

.. code-block:: python

    >>> def find_integer_quotient(row):
    ...     pairs = generate_pairs(row)
    ...
    ...     for pair in pairs:
    ...         is_integer, quotient = is_integer_quotient(pair)
    ...         if is_integer:
    ...             return int(quotient)
    ...
    ...     return -1

We do this across the rows with

.. code-block:: python

    >>> quotients = map(find_integer_quotient, rows)

Finally, we validate that all quotients are positive (recall that `find_integer_quotient` returns `-1` if an integer
quotient cannot be found).
