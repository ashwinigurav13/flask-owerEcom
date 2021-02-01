def make_decor(f1):
    def inner():
        print("Nitin")

    f1()
    return inner


@make_decor
def func():
    print("Hi")
