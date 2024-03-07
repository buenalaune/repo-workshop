import argparse
from repo_workshop import Fibonacci


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m repo_workshop` and `$ repo_workshop `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'n',
        type=int,
        help='Number to compute Fibonacci number for'
    )
    args = parser.parse_args()
    n = args.n
    fib_calculator = Fibonacci()
    fib_number = fib_calculator.fib(n)
    print(f"The fibonacci number of {n} is {fib_number}")
    ##########################
