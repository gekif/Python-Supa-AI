def decorator(func):
    def wrapper():
        print("Sebelum fungsi")
        func()
        print("Setelah fungsi")

    return wrapper


@decorator
def hello():
    print("Hello!")


hello()
