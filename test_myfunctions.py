from myfunctions import *
import pytest


# тестирование фукнции sum_string
@pytest.mark.parametrize("str1, str2", [("", "abc"), 
                                        ("abc", ""),
                                        ("abc", "def")])

def test_sum_str_ok(str1, str2):
    assert sum_string(str1, str2)

@pytest.mark.parametrize("str1, str2", [("abc", 2), 
                                        (2, "abc"), 
                                        (2, 2)])

def test_sum_str_err(str1, str2):
    try:
        sum_string(str1, str2)
    except TypeError:
        pass

# тестирование фукнции capital_letter
def test_capital_ok():
    assert capital_letter("abc") == 'A'
    assert capital_letter("ABC") == 'A'

def test_capital_err():
    try:
        capital_letter(1)
    except TypeError:
        pass


# тестирование фукнции union_set
def test_union_set_ok():
    assert union_set({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}

@pytest.mark.parametrize("set1, set2, expectation", [({1, 2, 3}, 2, TypeError),
                                                     (2, {1, 2, 3}, AttributeError)])

def test_union_set_err(set1, set2, expectation):
    try:
        union_set(set1, set2)
    except expectation:
        pass

# тестирование фукнции intersection_set
@pytest.mark.parametrize("set1, set2, expectation", [({1, 2, 3}, {1, 2, 3}, {1, 2, 3}), 
                                                    ({1, 5, 6}, {1, 7, 3}, {1}), 
                                                    ({1}, {2}, set())])

def test_intersection_set_ok(set1, set2, expectation):
    assert intersection_set(set1, set2) == expectation
 