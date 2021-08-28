def add(*args):
    result = 0
    for x in args:
        result += x

    return result


print(add(3, 5, 9, 17))


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)