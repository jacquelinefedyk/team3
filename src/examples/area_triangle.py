

def area_tr(base_t,height_t):
    """Calculates the area of a triangle with given base and height
    :Input: The base and height of the triangle (float, >=0)
    :Returns: The area of the triangle (float)."""
    if base_t < 0:
        raise ValueError("The base must be >= 0.")
    if height_t < 0:
        raise ValueError("The height must be >= 0.")

    area_out = 0.5 * base_t * height_t

    print("The area of a triangle with base b = {:3.2f}cm and height\
     h = {:3.2f}cm is A = {:4.2f}cm2".format(base_t,height_t,area_out))
    return area_out
