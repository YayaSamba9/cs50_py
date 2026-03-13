import pytest
from datetime import date
from seasons import Born
from seasons import convert


def test_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2000-01-01")
    result = Born.get()
    assert result == date(2000, 1, 1)


def test_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2000-13-01")
    with pytest.raises(SystemExit):
        Born.get()


def test_invalid_day(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2000-12-32")
    with pytest.raises(SystemExit):
        Born.get()


def test_invalid_format(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "01-01-2000")
    with pytest.raises(SystemExit):
        Born.get()


def test_convert():
    assert convert(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(1051200) == "One million, fifty-one thousand, two hundred minutes"