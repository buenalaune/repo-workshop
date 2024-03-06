import pytest
from repo_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from repo_workshop import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################