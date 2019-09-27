import random

from ZooAnimals.WakeUpBehavior import WakeUpBehavior

class Animal():
    """Primary Animal Class"""
    def __init__(self, name):
        self.name = name
        self.noise = "lets out an unearthy scream"
        self.wake_behavior = "rested"

    def wake_up(self):
        print(self.wake_behavior)
        self.wake_behav_obj = WakeUpBehavior(self.wake_behavior)
        return self.wake_behav_obj.wake_up(self.name, self.sub_type)

    def make_noise(self):
        return f"{self.name}, the {self.sub_type}, opens their mouth and {self.noise}."

    def eat_food(self, food_type="beans and rice"):
        return f"{self.name}, the {self.sub_type}, goes and mows down on some {food_type}."

    def roam(self):
        return f"{self.name}, the {self.sub_type}, wanders around aimlessly."

    def go_to_sleep(self):
        return f"{self.name}, the {self.sub_type}, nods off and catches some zs."

# ------------------ Felines ---------------------

class Feline(Animal):
    def __init__(self, name):
        super(Feline, self).__init__(name)
        self.super_type = "Feline"


    # Overriding Animal() method.
    def go_to_sleep(self):
        return f"{self.name}, the {self.sub_type}, finds the most comfy spot, donuts, and passes out."


class Cat(Feline):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.sub_type = "Cat"
        self.noise = 'meows'

    # Overriding Animal() method
    def make_noise(self):

        cat_choice = random.choice(["hair_ball", "make_noise", ""])

        if cat_choice != "make_noise":
            return self.hair_ball()
        else:
            print(f"{self.name}, the {self.sub_type}, decides to play along.")
            return super(Feline, self).make_noise()


    def hair_ball(self):

        return f"{self.name}, the {self.sub_type}, yaks up a hair ball instead."


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

    def go_to_sleep(self):
        return f"{self.name}, the {self.sub_type}, makes a sad whimper and then lays down."


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


# -------------------------------- Pachyderms --------------

class Pachyderm(Animal):
    def __init__(self, name):
        super(Pachyderm, self).__init__(name)
        self.super_type = "Pachyderm"


class Hippo(Pachyderm):
    def __init__(self, name):
        super(Hippo, self).__init__(name)
        self.sub_type = "Hippo"
        self.noise = "moos?"

    def go_to_sleep(self):
        return f"{self.name}, the {self.sub_type}, goes into the water, and dozes off."


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
