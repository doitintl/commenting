from inspect import getmembers, isfunction
from typing import Any

import pytest

import factorial

func_names = [function[0] for function in getmembers(factorial, isfunction) if function[0].startswith("factorial")]


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_zero(func_name):
    function = getattr(factorial, func_name)
    assert 1 == function(0)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_one(func_name):
    function = getattr(factorial, func_name)
    assert 1 == function(1)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_positive_int(func_name):
    function = getattr(factorial, func_name)
    assert 120 == function(5)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_int_as_float(func_name):
    try:
        function = getattr(factorial, func_name)
        assert 6.0 == function(3.0)
        # It's OK to return 6.0 as factorial(3.0)
    except (TypeError, AssertionError):
        pass
        # It's Ok  to refuse to process factorial(3.0)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_positive_nonint(func_name):
    """
    This fails for some implementations, which return a value here but shouldn't.
    This is left failing as an illustration that some implementations are flawed.
     """
    __expect_exception(func_name, 1.5)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_negative_int(func_name):
    """
    This fails for some implementations, which return a value here but shouldn't.
    This is left failing as an illustration that some implementations are flawed.
    """
    __expect_exception(func_name, -2)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_negative_nonint(func_name):
    """
    This fails for some implementations, which return a value here but shouldn't.
    This is left failing as an illustration that some implementations are flawed.
    """
    __expect_exception(func_name, -1.5)


@pytest.mark.parametrize("func_name", func_names)
def test_factorial_complex(func_name):
    __expect_exception(func_name, 1 + 1.0j)


def __expect_exception(func_name: str, x: Any):
    y = None
    try:
        function = getattr(factorial, func_name)
        y = function(x)
        succeeded = True
    except (TypeError, ValueError, AssertionError):  # icontract ViolationError is an AssertionError
        # Not using pytest.raises to gather  info on the value that was returned (but should not have been).
        succeeded = False

    assert not succeeded, f"Expected an error but {func_name}({x}) returned {y}"
