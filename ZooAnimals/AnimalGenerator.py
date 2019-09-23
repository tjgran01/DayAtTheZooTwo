from ZooAnimals.data.animal_names import animal_name_dict
from ZooAnimals.Animal import *
import random

class AnimalGenerator():
    def __init__(self, gen_method="one_of_each", num_animals=1):

        self.num_animals = num_animals
        self.animal_types = list(animal_name_dict.keys())
        self.gen_method = gen_method
        if gen_method == "one_of_each":
            self.num_animals = len(self.animal_types)


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
        if self.gen_method == "number_rand":
            for animal in range(self.num_ani_to_manage):
                type = random.choice(self.animal_types)
                animals_under_care.append(self.generate_animal(type))
        elif self.gen_method == "one_of_each":
            for type in self.animal_types:
                animals_under_care.append(self.generate_animal(type))

        return animals_under_care
