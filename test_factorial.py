from inspect import getmembers, isfunction
from typing import Callable, Any

import pytest

import factorial

func_names = [function[0] for function in getmembers(factorial, isfunction) if function[0].startswith("factorial")]


@pytest.mark.parametrize("func", func_names)
def test_factorial_zero(func):
    assert 1 == __func_by_name(func)(0)


@pytest.mark.parametrize("func", func_names)
def test_factorial_one(func):
    assert 1 == __func_by_name(func)(1)


@pytest.mark.parametrize("func", func_names)
def test_factorial_positive_int(func):
    assert 120 == __func_by_name(func)(5)


@pytest.mark.parametrize("func", func_names)
def test_factorial_int_as_float(func):
    try:
        assert 6.0 == __func_by_name(func)(3.0)
        # It's OK to return 6.0 as factorial(3.0)
    except (TypeError, AssertionError):
        pass
        # It's Ok  to refuse to process factorial(3.0)


@pytest.mark.parametrize("func", func_names)
def test_factorial_positive_nonint(func):
    """
    This fails for some implementations, that return a value here but shouldn't.
    This is left for illustration that some implementations are flawed.
    """
    __expect_exception(func, 1.5)


@pytest.mark.parametrize("func", func_names)
def test_factorial_negative_int(func):
    """
    This fails for some implementations, that return a value here but shouldn't.
    This is left for illustration that some implementations are flawed.
    """
    __expect_exception(func, -2)


@pytest.mark.parametrize("func", func_names)
def test_factorial_negative_nonint(func):
    """
    This fails for some implementations, that return a value here but shouldn't.
    This is left for illustration that some implementations are flawed.
    """
    __expect_exception(func, -1.5)


@pytest.mark.parametrize("func", func_names)
def test_factorial_complex(func):
    __expect_exception(func, 1 + 1.0j)


def __func_by_name(func: str) -> Callable:
    function = getattr(factorial, func)
    return function


def __expect_exception(func: str, x: Any):
    y = None
    try:
        y = __func_by_name(func)(x)
        succeed = True
    except (TypeError, ValueError, AssertionError):
        succeed = False  # Not using pytest.raises in order to gather more info

    assert not succeed, f"factorial{func}({x}) was {y}"
