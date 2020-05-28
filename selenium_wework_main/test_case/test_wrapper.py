from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """this is wrapper"""
        print("start")
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


class A:
    @timethis
    def tmp(self, a, b) -> str:
        """this is tmp"""
        print("tmp")
        return "hello"


def test_wrapper():
    print(A().tmp.__wrapped__(10, 20, 30))
