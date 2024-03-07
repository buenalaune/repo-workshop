import pytest
from repo_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from repo_workshop import Fibonacci
    except ImportError:
        assert False


def test_negative():
    try:
        fibonacci_calculator = Fibonacci()
        result = fibonacci_calculator.fib(-1)

    except ValueError:
        assert False


def test_numbers():
    tests = {
        5: 5
    }
    fibonacci_calculator = Fibonacci()
    for k, v in tests.items():
        if fibonacci_calculator.fib(k) != v:
            assert False

##### YOUR CODE HERE #####

##########################