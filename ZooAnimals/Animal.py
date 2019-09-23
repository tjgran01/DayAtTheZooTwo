import random

class Animal():
    """Primary Animal Class"""
    def __init__(self, name):
        self.name = name


    def wake_up(self):
        return f"I, {self.name}, have had a lovely nap. I am now awake."

    def make_noise(self, noise="snickers"):
        return f"{self.name}: opens their mouth and exclaims {noise}."

    def eat_food(self, food_type="beans and rice"):
        return f"{self.name} goes and mows down on some {food_type}."

    def roam(self):
        return f"{self.name} wanders around aimlessly."


class Feline(Animal):
    def __init__(self, name):
        super(Feline, self).__init__(name)
        self.super_type = "Feline"


class Cat(Feline):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.sub_type = "Cat"

    # Overriding parent method
    def make_noise(self):

        cat_choice = random.choice(["hair_ball", "make_noise", ""])

        if cat_choice != "make_noise":
            self.hair_ball()
        else:
            print(f"{self.name} decides to play along.")
            print(super(Feline, self).make_noise(noise="'Meow'"))


    def hair_ball(self):

        print(f"{self.name} yaks up a hair ball instead.")


class Canine(Animal):
    def __init__(self, name):
        super(Canine, self).__init__(name)
        self.super_type = "Canine"


class Dog(Canine):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.sub_type = "Dog"
