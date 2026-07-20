from hello import create_greeting


def test_create_greeting():
    assert create_greeting("Mona") == "Hello, Mona!"
