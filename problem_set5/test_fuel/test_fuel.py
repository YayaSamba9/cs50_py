from fuel import convert, gauge
import pytest

def test_valid_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_invalid_convert():
    with pytest.raises(ValueError):
       convert("2/1")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"

