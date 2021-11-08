# pytest python_homework/05_numpy_challenge/
import pytest  # noqa: F401; pylint: disable=unused-variable
from test_challenge import test_challenge

def test_value_to_standart():
    assert value_to_standart(10, 'C') == 10.0
