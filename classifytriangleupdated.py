"""Classify a triangle by the lengths of its sides."""
def classify_triangle(side_a, side_b, side_c):
    """Return the type of triangle for the given side lengths.

    Returns "not a triangle" for invalid input. Otherwise returns
    "equilateral", "isosceles" or "scalene", with " right" appended
    when the triangle is a right triangle.
    """
    # Check that the sides can actually form a triangle
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "not a triangle"

    if (side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a):
        return "not a triangle"

    # Determine the type based on side lengths
    distinct_sides = len({side_a, side_b, side_c})
    if distinct_sides == 1:
        triangle_type = "equilateral"
    elif distinct_sides == 2:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    # Check for right triangle
    sides = sorted([side_a, side_b, side_c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return triangle_type + " right"

    return triangle_type


if __name__ == "__main__": # pragma: no cover
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(2, 2, 3))
    print(classify_triangle(2, 3, 4))
