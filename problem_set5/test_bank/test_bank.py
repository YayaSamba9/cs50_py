from bank import value

def test_value_start_hello():
    assert value("hello") == 0
    assert value("hello, Friend")== 0
    assert value("HELLO") == 0


def test_value_startwith_h():
    assert value("how're you doing friend") == 20
    assert value("hi dear") == 20
    assert value("Hey") == 20


def test_value_something():
    assert value("What's happening")==100
    assert value("Good morning")== 100
