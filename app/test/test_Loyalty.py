from app.Loyalty import Loyalty


def test_Loyalty():
    result = Loyalty(1_000)

    assert 50 == result