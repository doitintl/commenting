def factorial1(p):
    return __iterative_factorial(p)


def factorial2(n):
    return __iterative_factorial(n)


def factorial3(n: int) -> int:
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."
    return __iterative_factorial(n)


def factorial4(n: int) -> int:
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."
    return __iterative_factorial(n)


def factorial5(n: int) -> int:
    """This simple  implementation of factorial by iterative multiplication supports non-negative integers only.
    Note that factorial of zero is defined as 1."""

    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."

    return __iterative_factorial(n)

def factorial6(n: int) -> int:
    from scipy.special import factorial as f
    return f(n)
    # Note deprecation warning

    # def factorial(n, exact=False):
    #     """
    #     The factorial of a number or array of numbers.
    #
    #     The factorial of non-negative integer `n` is the product of all
    #     positive integers less than or equal to `n`::
    #
    #         n! = n * (n - 1) * (n - 2) * ... * 1
    #
    #     Parameters
    #     ----------
    #     n : int or array_like of ints
    #         Input values.  If ``n < 0``, the return value is 0.

def factorial7(n: int) -> int:
    from  math  import factorial as f
    return f(n)

def __iterative_factorial(x):
    fact = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        fact *= i
    return fact




if __name__ == "__main__":

        for x in [ -2, -1.5, 0, 0.5, 1.3, 1.5, 2.8, 5, 6.8, 1 + 1.0j]:
            vals =[]
            vals_and_errors = []
            for func_number in range(1, 8):
                func_name = f"factorial{func_number}"
                factorial_func = globals()[func_name]

                try:
                    val = factorial_func(x)
                    vals.append(val)
                    vals_and_errors.append(str(val))
                except Exception as e:
                    vals_and_errors.append(type(e).__name__)

            print(f"factorial({x}): {', '.join(vals_and_errors)}")

