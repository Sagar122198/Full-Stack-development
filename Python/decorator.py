def my_decorator(func):
    def new():
        print("this is new function")
        func()
        print("func() is executed")
    return new
@my_decorator
def my_func():
    print("this is my_func()")

my_func()