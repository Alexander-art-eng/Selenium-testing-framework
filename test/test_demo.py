def add(x):
    return x + 1


def login():
    assert add(6) == 7


class TestCases:
    def test_first(self):
        assert add(3) == 4

    def test_second(self):
        assert add(4) == 6

    def test_third(self):
        assert add(5) == 6

