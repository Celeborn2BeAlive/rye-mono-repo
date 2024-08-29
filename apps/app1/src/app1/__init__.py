from package import hello as hello_package


def hello() -> str:
    return f"Hello from {hello_package()}!"
