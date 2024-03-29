from ZooAnimals.AnimalFactory import AnimalFactory
# ZooKeepers also have to wake up.
from ZooAnimals.WakeUpBehavior import WakeUpBehavior

class ZooKeeper():
    """
    An class that is given a set of animals to care for throughout the day.
    Args:
        *Optional* name[str]: A name for the ZooKeeper() object.
        *Optional*
    """
    def __init__(self, name="Zane", run_day_at_zoo=False):
        self.name = name
        # Factory Pattern
        self.animal_factory = AnimalFactory(gen_method="one_of_each")
        # Strategy Pattern
        self.wake_uper = WakeUpBehavior()
        # Observer Pattern
        self.observers = []

        # Method generated attributes here.
        self.animals_under_care = self.animal_factory.generate_animal_roster()
        self.num_animals_in_care = len(self.animals_under_care)

        # If you want to run DayAtTheZoo directly without external script.
        if run_day_at_zoo:
            # OH MY, ZooKeepers() can wake up too.
            print(self.wake_uper.wake_up(name))

            # --------------- Animal Stuff Here.
            self.broadcast_event(f"{self.name} is here everyone!")
            self.day_begins()
            self.broadcast_event(f"{self.name} is waking all the animals up! Check it out!")
            self.wake_up_animals()
            self.broadcast_event(f"{self.name} is now making sure all the animals are good to go!")
            self.perform_roll_call()
            self.broadcast_event(f"{self.name} is now running all those bad boys (and girls) around")
            self.exercise_animals()
            self.broadcast_event(f"{self.name} is about to feed them all! How cute.")
            self.feed_animals()
            self.broadcast_event(f"{self.name} is now going to put all the animals to bed. What a lovely day.")
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
              f"{self.num_animals_in_care} differenttalker animals.")
        print(f"Under {self.name}'s care today are:")
        self.display_animal_attrs()
        return f"{self.name} has made it to the zoo! OH golly folks."


    def wake_up_animals(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        wake_up() method and prints the result.
        """

        print("-" * 20)
        print(f"{self.name} goes to wake up the animals under his care.")
        self.animal_factory.set_wake_behaviors(self.animals_under_care)
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

    def feed_animals(self):
        """
        Prints a message and then calls all of the animals in self.animals_under_care's
        eat_food() method and prints the result.
        """
        print("-" * 20)
        print(f"{self.name} is now going to feed all the animals.")
        for animal in self.animals_under_care:
            print("-" * 20)
            print(f"{animal.eat_food()}")


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


# -------------------------------- Used for OBSERVER Pattern -------------------

    def broadcast_event(self, event):

        for observer in self.observers:
            observer.announce(event)


    def add_observer(self, observer):
        self.observers.append(observer)


    def remove_observer(self, observer):
        self.observers.remove(observer)



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
