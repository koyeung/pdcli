from pdcli.module1 import hello


def test_hello():
    """Check function hello."""

    result = hello("world")
    assert "hello world" == result
