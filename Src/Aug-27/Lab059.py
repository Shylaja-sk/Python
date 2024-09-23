import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"time taken by the function {end_time - start_time}")

    return wrapper()


@time_decorator
def test_Ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2) # to wait.

@time_decorator # reusing the code and to add extra functionality
def test_Ui_2():
    print("Add a function, time taken by this function")
    time.sleep(4)

