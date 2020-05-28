from functools import wraps


def f(a):
    def extend(fuc):
        @wraps(fuc)
        def hello(*args, **kwargs):
            print(a)
            print("hello")
            fuc(*args, **kwargs)
            print("good bye")
        return hello
    return extend


@f("AAAAAAAAAAAAA")
def tmp():
    print("tmp")


def tmp1():
    print("tmp1")


def test_wrapper():
    print(tmp())
