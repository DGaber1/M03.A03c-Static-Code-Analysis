def classify_triangle(a, b, c):
    # Check that the sides can actually form a triangle
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"

    # Determine the type based on side lengths
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    # Check for right triangle
    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return triangle_type + " right"

    return triangle_type
print(classify_triangle(3, 4, 5))
print(classify_triangle(1, 1, 1))
print(classify_triangle(2, 2, 3))
print(classify_triangle(2, 3, 4))