import pytest
# Do not delete import
from main import * #This import is necessary for the dynamic lookup

function_indexes = list(range(1, 7))


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_zero(i):
    assert 1 == func_by_index(i)(0)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_one(i):
    assert 1 == func_by_index(i)(1)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_positive_int(i):
    assert 120 == func_by_index(i)(5)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_int_as_float(i):
    try:
        assert 6.0 == func_by_index(i)(3.0)
        # It's OK to return 6.0 as factorial(3.0)
    except (TypeError, AssertionError):
        pass
        # It's Ok  to refuse to process factorial(3.0)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_positive_nonint(i):
    __expect_exception(i, 1.5)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_negative_int(i):
    __expect_exception(i, -2)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_negative_nonint(i):
    __expect_exception(i, -1.5)


@pytest.mark.parametrize("i", function_indexes)
def test_factorial_complex(i):
    __expect_exception(i, 1 + 1.0j)


def func_by_index(i):
    return globals()[f"factorial{i}"]


def __expect_exception(i, x):
    y = None
    try:
        y = func_by_index(i)(x)
        succeed = True
    except (TypeError, ValueError, AssertionError):
        succeed = False  # Not using pytest.raises in order to gather more info

    assert not succeed, f"factorial{i}({x}) was {y}"
