import pytest

from practice import *
import math


def test_max_of_3():
    assert max_of_3(2, 3, 4) == 4


def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5)


def test_count_spaces():
    assert count_spaces("Maria Silva") == 1


def test_count_passing_grades():
    assert count_passing_grades([8, 10, 8, 4, 0, 7, 5], 6) == 4


def test_curve_these_grades():
    grades = [2, 3, 4]
    curve_these_grades(grades, 1)
    assert grades == [3, 4, 5]


def test_create_new_curved_grades():
    assert create_new_curved_grades([2, 3, 4], 1) == [3, 4, 5]


def test_avg_of_grades():
    assert math.isclose(avg_of_grades([3, 4, 5], False), 4)


def test_failing_grade_indexes():
    assert create_failing_grade_indexes([8, 5, 9, 10, 4], 6) == [1, 4]


def test_make_initials():
    assert make_initials("Maria Silva") == "MS"
