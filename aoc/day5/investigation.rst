Day Five
========

Task
----

Suppose that we have the following *maze*:

.. code-block:: python

    >>> m = [0, 3, 0, 1, -3]

Each element in the maze corresponds to a movement instruction (for example, `0` means don't move, `3` means move
three to the right and `-3` means move 3 to the left).

Each time you follow a movement instruction, the instruction just executed changes. In part one, it increments by `1`
and in part two, it increments by `1` if it is less than or equal to `3`, else it decrements by `1`.

The task_ is to, starting at the first element, follow the instructions until you have escaped the maze.

.. _task: https://adventofcode.com/2017/day/5

Implementation
--------------

Part One
~~~~~~~~

First, we want a function that implements `jump`, where `jump` is the movement instruction defined above.

.. code-block:: python

    >>> def jump(maze, from_position):
    ...     return (
    ...         [x + 1 if i == from_position else x for i, x in enumerate(maze)],
    ...         from_position + maze[from_position]
    ...     )

This returns a tuple where the first element is the new maze and the second element is our position within it. For
example,

.. code-block:: python

    >>> jump(maze=m, from_position=0)
    ([1, 3, 0, 1, -3], 0)

Then we can count how many steps is takes to leave as follows:

.. code-block:: python

    >>> steps = 0
    >>> from_position = 0
    >>> while 0 <= from_position < len(m):
    ...     m, from_position = jump(m, from_position)
    ...     steps += 1
    >>> steps
    5

Part Two
~~~~~~~~

In part two, the rule for updating the instruction changes. Now, we must increment by `1` if the instruction is less
than or equal to `3`, else decrement by `1`. We can update our jump definition accordingly.

.. code-block:: python

    >>> def jump(maze, from_position):
    ...     if maze[from_position] < 3:
    ...         new_position = maze[from_position] + 1
    ...     else:
    ...         new_position = maze[from_position] - 1
    ...
    ...     return (
    ...         [new_position if i == from_position else x for i, x in enumerate(maze)],
    ...         from_position + maze[from_position]
    ...     )

It's a bit messy but rather than refactor immediately, we have a performance issue to address...

Optimisation
~~~~~~~~~~~~

Currently whenever we `jump`, we create a new maze rather than modifying the existing one. In general I think this
makes for more readable and safer code.

That being said, this code is taking a long time to run; around 30 seconds for the first part and around 30 minutes
for the second! Let's try modifying the existing list to see how that changes things.

.. code-block:: python

    >>> def jump(maze, from_position):
    ...     maze[from_position] += 1
    ...     return from_position + maze[from_position]

It definitely improves things but it's difficult to say by precisely how much (due to poor benchmarking; more on this
in a second). Changing both parts to modify in place means that the test suite runs in around 12 seconds. That's
good enough for now.

Benchmarking
~~~~~~~~~~~~

Just a quick note on benchmarking. Currently the only timed run I have is the test suite (`python setup.py test`). This
is too high level to effectively identify issues with functions and optimise there. On the advice of a friend_, I'm
jumping into Jupyter notebooks with the hope of making profiling easier going forward.

.. _friend: https://github.com/jrdurrant/adventofcode
