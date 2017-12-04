Day Four
========

Task
----

The task_ is to validate a passphrase according to some rules.

The first rule is that a passphrase should contain no duplicate words.

The second rule is that a passphrase should not contain any elements that are an anagram of any othersG

.. _task: https://adventofcode.com/2017/day/4

Implementation
--------------

Part One
~~~~~~~~

Since I'm implementing this in Python, I'll use the fact that if the set and list of some iterable have the same
length, then every item in the set must be unique (or at least the hash of each element is, but that should be
sufficient for this use case).

.. code-block:: python

    >>> def contains_unique_elements(list):
    ...     return True if len(list) == len(set(list)) else return False

For example,

.. code-block:: python

    >>> contains_unique_elements(["aa", "bb", "cc", "dd", "ee"])
    True

    >>> contains_unique_elements(["aa", "bb", "cc", "dd", "aa"])
    True

Then, given a list of passphrases, we can determine the number that are valid.

.. code-block:: python

    >>> passphrases = [["aa", "bb", "cc", "dd", "ee"], ["aa", "bb", "cc", "dd", "aa"]]
    >>> number_valid = sum(map(contains_unique_elements, [["aa"], ["bb"]]))
    >>> number_valid
    2

Part Two
~~~~~~~~

Now, we need a way of determining whether a list contains any elements that are an anagram of any others. First, let's
talk about identifying this in the case where we have just a pair of strings. In such a case, if we order the strings
and compare, one is an anagram of the other if this comparison yields equality.

.. code-block:: python

    >>> def is_anagram(str_a, str_b):
    ...     return ''.join(sorted(str_a)) == ''.join(sorted(str_b))

    >>> is_anagram('foo', 'bar')
    False

    >>> is_anagram('foo', 'oof')
    True

We need to do this across the list. Since the comparison is bidirectional, we only need to compare an element with all
elements after it.

.. code-block:: python

    >>> def contains_no_anagrams(l):
    ...     for index, element in enumerate(l):
    ...         for otherElement in l[index + 1:]:
    ...             if is_anagram(element, otherElement):
    ...                 return False
    ...     return True

    >>> contains_no_anagrams(['foo', 'bar', 'baz'])
    True

    >>> contains_no_anagrams(['foo', 'bar', 'baz', 'oof'])
    False
