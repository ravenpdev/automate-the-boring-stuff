import pytest
import src.demo as demo


def test_add():
    result = demo.add(1, 4)
    assert result == 5


def test_divide():
    result = demo.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        _ = demo.divide(10, 0)


def test_add_strings():
    result = demo.add("i like ", "burgers")
    assert result == "i like burgers"
