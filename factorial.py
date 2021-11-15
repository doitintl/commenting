def fact(p):
    return __iterative_factorial(p)


def factorial_basic(p):
    return __iterative_factorial(p)


def factorial_param_name(n):
    return __iterative_factorial(n)


def factorial_type_hints(n: int) -> int:
    return __iterative_factorial(n)


def factorial_assertions(n: int) -> int:
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."
    return __iterative_factorial(n)


def factorial_with_comment_for_internal_consumptin(n: int) -> int:
    """
    This is a simple iterative implementation of factorial.
    The input must be a non-negative integer.
    Note that factorial of zero is defined as 1.
    """
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."
    return __iterative_factorial(n)


def factorial_for_public_api(n: int) -> int:
    """
    This implements x! (factorial), the product of all numbers from 1 up to and including n.
    :param n A nonnegative integer
    :return The factorial; note that for 0, this returns 1.
    """
    return __iterative_factorial(n)


def factorial_scipi(n: int) -> int:
    from scipy.special import factorial as f
    return f(n)


def factorial_math(n: int) -> int:
    from math import factorial as f
    return f(n)


def factorial_doctest(n) -> int:
    """
    Run doctests with python -m doctest -v factorial.py

    >>> factorial_doctest(3)
    6
    >>> factorial_doctest(0)
    1
    >>> factorial_doctest(1.5)
    Traceback (most recent call last):
      ...
    TypeError: 'float' object cannot be interpreted as an integer
    """
    return __iterative_factorial(n)


def __iterative_factorial(x):
    ret = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        ret *= i
    return ret
