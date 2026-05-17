from student_code.solution import add

def test_basic():
    assert add(1, 2) == 3

def test_negative():
    assert add(-1, 1) == 0
