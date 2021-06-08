class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('walk')


m = Mammal()

# In this example, our animal class has this constructor where we initialize the age attribute to 1.

print(m.age)
