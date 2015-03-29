Source Example
==============

Source1 provides functions for describing a triangle.

Determining Triangle Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source1.get_triangle_type` provides users with a way to provide a set of three sides
of a triangle and returns the type of triangle ("equilateral", "isosceles", "scalene" or "invalid")

Scalene Example
^^^^^^^^^^^^^^^

>>> from source.source1 import get_triangle_type
>>> get_triangle_type(1, 2, 3)
'scalene'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source1
    :members: