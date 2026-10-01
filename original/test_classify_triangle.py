from original.classify_triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(5, 5, 5) == "equilateral"
def test_equilateral_different_size():
    assert classify_triangle(10, 10, 10) == "equilateral"
def test_isosceles_first_two_equal():
    assert classify_triangle(5, 5, 3) == "isosceles"
def test_isosceles_first_and_third_equal():
    assert classify_triangle(5, 3, 5) == "isosceles"
def test_isosceles_last_two_equal():
    assert classify_triangle(3, 5, 5) == "isosceles"
def test_scalene():
    assert classify_triangle(2, 3, 4) == "scalene"
def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "scalene right"
def test_right_triangle_reversed():
    assert classify_triangle(5, 4, 3) == "scalene right"
def test_larger_right_triangle():
    assert classify_triangle(5, 12, 13) == "scalene right"
def test_invalid_triangle():
    assert classify_triangle(1, 2, 10) == "not a triangle"
def test_degenerate_triangle():
    assert classify_triangle(1, 1, 2) == "not a triangle"
def test_zero_side():
    assert classify_triangle(0, 5, 5) == "not a triangle"
def test_negative_side():
    assert classify_triangle(-1, 5, 5) == "not a triangle"