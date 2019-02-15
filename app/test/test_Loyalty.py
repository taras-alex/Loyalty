from app.Loyalty import Loyalty


def test_Loyalty():
    result = Loyalty(0, 0)

    assert 0 == result


def test_Loyalty1():
    result = Loyalty(200_000, 200_000)

    assert 2_0000 == result

def test_Loyalty2():
    result = Loyalty(0, 200_000)

    assert 1_0000 == result