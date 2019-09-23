import random

class Animal():
    """Primary Animal Class"""
    def __init__(self, name):
        self.name = name
        self.noise = "snickers"


    def wake_up(self):
        return f"I, {self.name}, have had a lovely nap. I am now awake."

    def make_noise(self):
        return f"{self.name}: opens their mouth and exclaims {self.noise}."

    def eat_food(self, food_type="beans and rice"):
        return f"{self.name} goes and mows down on some {food_type}."

    def roam(self):
        return f"{self.name} wanders around aimlessly."


# ------------------ Felines ---------------------

class Feline(Animal):
    def __init__(self, name):
        super(Feline, self).__init__(name)
        self.super_type = "Feline"


class Cat(Feline):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.sub_type = "Cat"
        self.noise = 'meows'

    # Overriding parent method
    def make_noise(self):

        cat_choice = random.choice(["hair_ball", "make_noise", ""])

        if cat_choice != "make_noise":
            self.hair_ball()
        else:
            print(f"{self.name} decides to play along.")
            print(super(Feline, self).make_noise())


    def hair_ball(self):

        print(f"{self.name} yaks up a hair ball instead.")


class Lion(Feline):
    def __init__(self, name):
        super(Lion, self).__init__(name)
        self.sub_type = "Lion"
        self.noise = 'rawrs'


class Tiger(Feline):
    def __init__(self, name):
        super(Tiger, self).__init__(name)
        self.sub_type = "Tiger"
        self.noise = 'rawrs'


# ------------------------------ Canines


class Canine(Animal):
    def __init__(self, name):
        super(Canine, self).__init__(name)
        self.super_type = "Canine"


class Dog(Canine):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.sub_type = "Dog"
        self.noise = "borks"


class Wolf(Canine):
    def __init__(self, name):
        super(Wolf, self).__init__(name)
        self.sub_type = "Wolf"
        self.noise = "yips"


# -------------------------------- Pachyderms

class Pachyderm(Animal):
    def __init__(self, name):
        super(Pachyderm, self).__init__(name)
        self.super_type = "Pachyderm"


class Hippo(Pachyderm):
    def __init__(self, name):
        super(Hippo, self).__init__(name)
        self.sub_type = "Hippo"
        self.noise = "moos?"


class Elephant(Pachyderm):
    def __init__(self, name):
        super(Elephant, self).__init__(name)
        self.sub_type = "Elephant"
        self.noise = "trumpets"


class Rhino(Pachyderm):
    def __init__(self, name):
        super(Rhino, self).__init__(name)
        self.sub_type = "Rhino"
        self.noise = "grunts, gutterally"
