#pytest python_homework/nucleid_acids_tool


import pytest
from .nucleid_acids_01 import function_test

def test_function_test():
    assert function_test(3) == 6
    