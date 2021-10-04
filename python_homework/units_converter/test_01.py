# pytest python_homework/units_converter
import pytest  # noqa: F401; pylint: disable=unused-variable
from .units_converter import value_to_standart, convert_temperature


def test_value_to_standart():
    assert value_to_standart(10, 'C') == 10.0
    assert round(value_to_standart(-30, 'F'), 2) == -34.44
    assert round(value_to_standart(200, 'K'), 2) == -73.15
    assert value_to_standart(0, 'Ra') == -273.15
    assert round(value_to_standart(6, 'Ra'), 1) == -269.8


def test_convert_temperature():
    assert [round(num, 2) for num in convert_temperature(0)] == [0.00, 273.15, 32.00, 491.67, 0]
