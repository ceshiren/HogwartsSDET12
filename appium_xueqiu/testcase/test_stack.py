import inspect


def a():
    print(inspect.stack()[2].function)
    print("a")


def b():
    a()


def test_stack():
    b()
