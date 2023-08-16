#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Summing up tuples

        Args:
            tuple_a: First tuple
            tuple_b: second tuple

        Returns:
            Returns new tuple
    """

    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    a = tuple_a[0]
    b = tuple_a[1]
    c = tuple_b[0]
    d = tuple_b[1]

    e, f = a + c, b + d
    new_tuple = (e, f)

    return new_tuple
