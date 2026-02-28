from um import count

def test_count1():
    assert count('um') == 1
    assert count('Um... what are regular expressions?')==1
    assert count('This is, um... CS50')==1
    assert count('Hello, um, world')==1

def test_count2():
    assert count('um, yahya')== 1

def test_count3():
    assert count('um um um ')== 3

def test_count4():
    assert count('umbrella') == 0

def test_count5():
    assert count('Hello, world')== 0

def test_count():
    assert count('Um, Thanks, um, regular expressions make sens now')==2
    assert count('Um?, Mum? Is this that album where, um, umm, the clumsy alums play drums')== 2
