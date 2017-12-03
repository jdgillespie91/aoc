Day Three
=========

Task
----

The task_ is to find the shortest distance between two points in a grid. One of these points is fixed (as 1 in the
following grid and as `(0, 0)` in my coordinate system).

Each point on the grid is described by an integer allocated by starting at 1 and then incrementing whilst spiralling
outwards. For example,

.. code-block::

    5 4 3
    6 1 2
    7 8 9
    ...

Movements are restricted to up, down, left and right. For example, given an input `5`, the output should be `2`, since
the shortest distance is two steps (for example, right then down).

.. _task: https://adventofcode.com/2017/day/3

Implementation
--------------

Part One
~~~~~~~~

Suppose that we have some input `n`. We can quickly identify the square in which it lies by comparing with the
values in the bottom-right diagonal, the sequence of odd square numbers.

For example, suppose we have `12` as the input. Then since `12` is greater than `9` but less than `25` we know it must
lie in the square made by the integers between `10` and `25` inclusive. Counting outwards, this is the second square
(starting at zero).

.. code-block:: python

    >>> def find_square_index(n):
    ...     i = 0
    ...     root = 2 * i + 1
    ...
    ...     while n > root * root:
    ...         i += 1
    ...         root = 2 * i + 1
    ...
    ...     return i

For example,

.. code-block:: python

    >>> n = 12
    >>> i = find_square_index(n)
    >>> i
    2

Now, we need to identify the coordinates of the square in which the input lies. We can generate the sequence of
coordinates, in order from smallest integer to largest, as follows

.. code-block:: python

    >>> def generate_square_sequence(i):
    ...     if i == 0:
    ...         return [(0, 0)]
    ...
    ...     seq = deque([i] * (2 * i - 1) + list(range(i, -i - 1, -1)) + [-i] * (2 * i - 1) + list(range(-i, i + 1)))
    ...
    ...     x = seq.copy()
    ...     y = seq.copy()
    ...     y.rotate(2 * i)
    ...
    ...     return list(zip(x, y))

For example,

.. code-block:: python

    >>> seq = generate_square_sequence(i)
    >>> seq
    [
        (2, -1), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2), (-2, 2), (-2, 1),
        (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2)
    ]

We can determine the coordinate of the input by counting along this sequence.

.. code-block:: python

    >>> difference = n - (2 * i - 1) * (2 * i - 1)
    >>> coordinates = seq[difference - 1]
    >>> coordinates
    (2, 1)

Finally, the distance is given by summing the magnitude of the coordinates.

.. code-block:: python

    >>> distance = abs(coordinates[0]) + abs(coordinates[1])
    >>> distance
    3
