def fact(p):
    return __iterative_factorial(p)

# Naming functions factorial1, factorial2, etc is not a good idea. I do that here simply because
# these are different versions of the same thing, with various improvements.
def factorial_basic(p):
    return __iterative_factorial(p)


def factorial_param_name(n):
    return __iterative_factorial(n)


def factorial_typehints(n: int) -> int:
    return __iterative_factorial(n)


def factorial_assertions(n: int) -> int:
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."
    return __iterative_factorial(n)

def factorial_for_public_API(n: int) -> int:
    """
    :param n A nonnegative integer
    :return The product of all integers from 1 up to and including n; or for 0, return 1.
    """
    return __iterative_factorial(n)

def factorial_with_comment(n: int) -> int:
    """
    This is a simple iterative implementation of factorial.
    The input must be a non-negative integer.
    Note that factorial of zero is defined as 1.
    """
    assert isinstance(n, int), f"{n} is not an integer and so unsupported."
    assert n >= 0, f"{n} is negative and so unsupported."

    return __iterative_factorial(n)

def factorial_scipi(n: int) -> int:
    from scipy.special import factorial as f
    return f(n)


def factorial_math(n: int) -> int:
    from  math  import factorial as f
    return f(n)

def __iterative_factorial(x):
    ret = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        ret *= i
    return ret



if __name__ == "__main__":
        """Print out values for debugging. See test_factorial.py for a more formal test."""
        factorial_functions = [f for f in globals().keys() if f.startswith("factorial")]
        print(",", ", ".join(factorial_functions))

        for x in [ -2, -1.5, 0, 0.5, 1.3, 1.5, 2.8, 5, 6.8, 1 + 1.0j]:
            vals =[]
            vals_and_errors = []
            for func_name in factorial_functions:
                factorial_func = globals()[func_name]

                try:
                    val = factorial_func(x)
                    vals.append(val)
                    vals_and_errors.append(str(val))
                except Exception as e:
                    vals_and_errors.append(type(e).__name__)

            print(f"{x}: {', '.join(vals_and_errors)}")

