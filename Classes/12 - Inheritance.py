class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eating')


class Mammal(Animal):
    def walk(self):
        print('walking')


class Fish(Animal):
    def swim(self):
        print('swimming')


m = Mammal()

print(m.__dict__)
