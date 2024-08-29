from app1 import hello, hello_package


def test_hello():
    assert hello() == f"Hello from {hello_package()}!"
