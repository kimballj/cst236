"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""

def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = b[1]
        a = a[1]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"