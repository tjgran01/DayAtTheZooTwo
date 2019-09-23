from ZooAnimals.AnimalGenerator import AnimalGenerator

class ZooKeeper():
    """
    An class that is given a set of animals to care for throughout the day.
    Args:
        *Optional* name[str]: A name for the ZooKeeper() object.
        *Optional*
    """
    def __init__(self, name="Zane", run_day_at_zoo=False):
        self.name = name
        self.animal_generator = AnimalGenerator(gen_method="one_of_each")

        # Method generated attributes here.
        self.animals_under_care = self.animal_generator.generate_animal_roster()
        self.num_animals_in_care = len(self.animals_under_care)

        # If you want to run DayAtTheZoo directly without external script.
        if run_day_at_zoo:
            self.day_begins()
            self.wake_up_animals()
            self.perform_roll_call()
            self.exercise_animals()
            self.shut_down_the_zoo()


# -------------------------------- Used for running DayAtTheZoo ----------------


    def day_begins(self):
        """
        Prints messages to the user about the ZooKeeper()'s name.
        And also tells the user how many Animals() are under the ZooKeepers()
        care.
        """

        print(f"{self.name}, the Zoo Keeper, is beginning his day at the Zoo.")
        print(f"Today, {self.name} is responsible for "
              f"{self.num_animals_in_care} different animals.")
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
