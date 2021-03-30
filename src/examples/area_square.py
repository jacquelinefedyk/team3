def area_squa(l):
    """Calculates the area of a square with given side length l.

    :Input: Side length of the square l (float, >=0)
    :Returns: Area of the square A (float)."""

    if l < 0:
        raise ValueError("The side length must be >= 0.")

    A = l**2
    return A
