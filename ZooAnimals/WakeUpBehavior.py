# Wake Behaviors are delegated to the WakeUpBehavior() Class.
# It's also been delegated to by the ZooKeeper(), just to show how cool it is.

class WakeUpBehavior():
    """An Object that Uses the Strategy Pattern to offload different
    Behaviors from"""
    def __init__(self, wake_behavior="rested"):
        self.wake_behavior = wake_behavior


    def wake_up(self, name, subtype=None):
        """Returns a string pertaining to the mood of being woken up.
        Args:
            name[str]: The name of the creature waking up.
            subtype[str]: The species of animal waking up.
        """

        if subtype:
            if self.wake_behavior == "rested":
                return f"I, {name}, the {subtype}, have had a lovely nap. I am now awake."
            elif self.wake_behavior == "grumpy":
                return f"I, {name}, the {subtype}, cannot BELIEVE YOU HAVE WOKEN ME FROM MY NAP."
            elif self.wake_behavior == "energized":
                return f"I, {name}, the {subtype}, am so JAZZED right now!"
            else:
                return f"I, {name}, the {subtype}, need a cup of coffee."
        else:
            return f"Just another day in paradise, Thinks {name}, as they wake up."
