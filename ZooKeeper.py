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
    def __init__(self, name="Zane", num_ani_to_manage=26, run_day_at_zoo=False):

        # Stock Attributes here.
        self.name = name
        self.num_ani_to_manage = num_ani_to_manage
        self.animal_types = ["Dog", "Cat", "Tiger", "Lyon", "Wolf", "Hippo"
                             "Elephant", "Rhino"]

        # Method generated attributes here.
        self.animals_under_care = self.generate_animal_roster()

        # If you want to run DayAtTheZoo directly without external script.
        if run_day_at_zoo:
            pass


# ---------------------- Needed for Init ---------------------------------------

    def day_begins(self):
        """
        Prints messages to the user about the ZooKeeper()'s name.
        And also tells the user how many Animals() are under the ZooKeepers()
        care.
        """

        print(f"{self.name}, the ZooKeeper is beginning his day at the Zoo.")
        print(f"Today, {self.name} is responsible for "
              f"{self.num_ani_to_manage} different animals.")


    def generate_animal_roster(self):
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
        for animal in range(self.num_ani_to_manage):
            # Stop this from being random at some point.
            type = random.choice(self.animal_types)

            if type == "Dog":
                animals_under_care.append(Dog(random.choice(animal_name_dict["Dog"])))
            elif type == "Cat":
                animals_under_care.append(Cat(random.choice(animal_name_dict["Dog"])))
            elif type == "Lion":
                animals_under_care.append(Lion(random.choice(animal_name_dict["Lion"])))
            elif type == "Tiger":
                animals_under_care.append(Lion(random.choice(animal_name_dict["Tiger"])))
            elif type == "Wolf":
                animals_under_care.append(Wolf(random.choice(animal_name_dict["Wolf"])))
            elif type == "Hippo":
                animals_under_care.append(Hippo(random.choice(animal_name_dict["Hippo"])))
            elif type == "Elephant":
                animals_under_care.append(Elephant(random.choice(animal_name_dict["Elephant"])))
            elif type == "Rhino":
                animals_under_care.append(Rhino(random.choice(animal_name_dict["Rhino"])))

            else:
                pass

        return animals_under_care


# -------------------------------- Used for debugging --------------------------


    def display_animal_attrs(self):
        """
        Displays name, super_type, and sub_type attributes of each animal
        within the ZooKeeper()'s care.

        """

        for indx, animal in enumerate(self.animals_under_care):
            print(f"Animal #{indx + 1}")
            print(animal.name)
            print(animal.super_type)
            print(animal.sub_type)
            print("-" * 20)



zane = ZooKeeper("Zane")
zane.display_animal_attrs()
