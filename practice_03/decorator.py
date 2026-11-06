def announce(func):
    def wrapper():
        print("Начинаем")
        return func()
    return wrapper

@announce
def hello():
    print("Привет!")

hello()

