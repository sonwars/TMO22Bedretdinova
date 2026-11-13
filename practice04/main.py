print("Задание 1")
x = 11

def show():
    x = 1
    print(x)

show()
print(x)

#Внутри функции show() используется локальная переменная x = 1. 
#Она создается в момент вызова функции и удаляется после её завершения.
#Снаружи используется глобальная (внешняя) переменная x = 11. 
#Функция не изменила внешнюю переменную, она создала свою собственную внутри себя.

print("Задание 2 ")
def total(*args):
    return sum(args)

print(total(1, 2, 3))

print("Задание 3")
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Анна", age=17))

print("Задание 4")
def increase(x):
    return x + 1

def apply(func, value):
    return func(value)

print(apply(increase, 2))

print("Задание 5")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(2)