from ZooAnimals.Animal import *
from ZooAnimals.data.animal_names import animal_name_dict
import random


class ZooKeeper():
    """
    An class that is given a set of animals to care for throughout the day.
    Args:
        *Optional* name[str]: A name for the ZooKeeper() object.
        *Optional* num_ani_to_manage[str]: A name for the ZooKeeper() object.
    """
    def __init__(self, name="Zane", num_ani_to_manage=26,
                 animal_gen_method="one_of_each", run_day_at_zoo=False):

        # Stock Attributes here.
        self.animal_types = ["Dog", "Cat", "Tiger", "Lion", "Wolf", "Hippo",
                             "Elephant", "Rhino"]
        self.name = name
        self.num_ani_to_manage = num_ani_to_manage
        if animal_gen_method == "one_of_each":
            self.num_ani_to_manage = len(self.animal_types)


        # Method generated attributes here.
        self.animals_under_care = self.generate_animal_roster(generation_method=animal_gen_method)

        # If you want to run DayAtTheZoo directly without external script.
        if run_day_at_zoo:
            self.day_begins()
            self.wake_up_animals()
            self.perform_roll_call()
            self.exercise_animals()
            self.shut_down_the_zoo()


# ---------------------- Needed for Init ---------------------------------------

    def generate_animal(self, type):
        """
        Generates an animal with a random name based on the type passed.
        Args:
            type[str]: The type of animal to be generated.
        Returns
            Animal()[object]: The animal object.
        """
    # Could fix this to animal_name_dict[f"{type}"].
        if type == "Dog":
            return Dog(random.choice(animal_name_dict["Dog"]))
        elif type == "Cat":
            return Cat(random.choice(animal_name_dict["Dog"]))
        elif type == "Lion":
            return Lion(random.choice(animal_name_dict["Lion"]))
        elif type == "Tiger":
            return Tiger(random.choice(animal_name_dict["Tiger"]))
        elif type == "Wolf":
            return Wolf(random.choice(animal_name_dict["Wolf"]))
        elif type == "Hippo":
            return Hippo(random.choice(animal_name_dict["Hippo"]))
        elif type == "Elephant":
            return Elephant(random.choice(animal_name_dict["Elephant"]))
        elif type == "Rhino":
            return Rhino(random.choice(animal_name_dict["Rhino"]))
        else:
            raise TypeError(f"Type of animal {type} does not currently exist.")



    def generate_animal_roster(self, generation_method="one_of_each"):
        """
        Creates the Animals that are under the ZooKeepers() care for the day.

        Args:
            self(self.num_ani_to_manage)[int]: The number of animals under the
            ZooKeeper()'s care.
            self(self.animal_types)[List]: The types of animal the ZooKeeper will
            care for.
        Returns:
            animals_under_care[List]: The Animal() objects the ZooKeeper will care
            for.
        """

        animals_under_care = []
        if generation_method == "number_rand":
            for animal in range(self.num_ani_to_manage):
                type = random.choice(self.animal_types)
                animals_under_care.append(self.generate_animal(type))
        elif generation_method == "one_of_each":
            for type in self.animal_types:
                animals_under_care.append(self.generate_animal(type))

        return animals_under_care


# -------------------------------- Used for running DayAtTheZoo ----------------


    def day_begins(self):
        """
        Prints messages to the user about the ZooKeeper()'s name.
        And also tells the user how many Animals() are under the ZooKeepers()
        care.
        """

        print(f"{self.name}, the Zoo Keeper, is beginning his day at the Zoo.")
        print(f"Today, {self.name} is responsible for "
              f"{self.num_ani_to_manage} different animals.")
        print(f"Under {self.name}'s care today are:")
        self.display_animal_attrs()



    def wake_up_animals(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        wake_up() method and prints the result.
        """

        print("-" * 20)
        print(f"{self.name} goes to wake up the animals under his care.")
        for animal in self.animals_under_care:
            print("-" * 20)
            print(f"{self.name} goes to wake up, {animal.name}, the {animal.sub_type}!")
            print(animal.wake_up())


    def perform_roll_call(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        make_noise() method and prints the result.

        ***The Cat()'s make_noise method is overridden and sometime the cat (66%) of
        the time will yak up a hairball instead.
        """

        print("-" * 20)
        print(f"{self.name} performs roll call on the animals under his care.")
        for animal in self.animals_under_care:
            print("-" * 20)
            print(f"{animal.make_noise()}")


    def exercise_animals(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        roam() method and prints the result.
        """

        print("-" * 20)
        print(f"{self.name} helps the animals pump some iron (work out).")
        for animal in self.animals_under_care:
            print("-" * 20)
            print(f"{animal.roam()}")


    def shut_down_the_zoo(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        roam() method and prints the result.
        """

        print("-" * 20)
        print(f"{self.name} begins closing the zoo, and putting the animals to bed.")
        for animal in self.animals_under_care:
            print("-" * 20)
            print(f"{animal.go_to_sleep()}")

# -------------------------------- Used for debugging --------------------------


    def display_animal_attrs(self):
        """
        Displays name, super_type, and sub_type attributes of each animal
        within the ZooKeeper()'s care.
        """

        for indx, animal in enumerate(self.animals_under_care):
            print("-" * 20)
            print(f"Animal #{indx + 1}")
            print(f"Name: {animal.name}")
            print(f"Super Type: {animal.super_type}")
            print(f"Sub Type: {animal.sub_type}")



zane = ZooKeeper("Zane", run_day_at_zoo=True)
