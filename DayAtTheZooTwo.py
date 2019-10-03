from ZooKeeper import ZooKeeper
from ZooAnnouncer import ZooAnnouncer

# Generation of animals is handled in ZooKeeper().__init__() method.
# because A ZooKeeper() is pretty useless without a collection of Animals to keep.
zooey = ZooKeeper(name="Zooey")

zelda = ZooAnnouncer(name="Zelda")
# Zelda is added to Zooey's oberser list.
# Now, whenever Zooey broadcasts an event Zooey can listen.
zelda.observe_keeper(zooey)

# ZooKeeper does Zoo Stuff.
zooey.broadcast_event(f"{zooey.name} is here everyone!")
zooey.day_begins()
zooey.broadcast_event(f"{zooey.name} is waking all the animals up! Check it out!")
zooey.wake_up_animals()
zooey.broadcast_event(f"{zooey.name} is now making sure all the animals are good to go!")
zooey.perform_roll_call()
zooey.broadcast_event(f"{zooey.name} is now running all those bad boys (and girls) around")
zooey.exercise_animals()
zooey.broadcast_event(f"{zooey.name} is about to feed them all! How cute.")
zooey.feed_animals()
zooey.broadcast_event(f"{zooey.name} is now going to put all the animals to bed. What a lovely day.")
zooey.shut_down_the_zoo()

# Observer stuff.

for x in range(3):
    print("\n")

print("Before observing ceases.")
# This is why I love f strings.
print(f"{[observer.name for observer in zooey.observers]}") # Should have zelda
print(f"{[observing.name for observing in zelda.currently_observing]}") # Should have Zooey

zelda.cease_observing_keeper(zooey) # ZooAnnouncer stops being a creep.

for x in range(2):
    print("\n")

print("After observing is ceased.")
print(f"{zooey.observers}") # Should be empty
print(f"{zelda.currently_observing}") # Should be empty

# gc will already handle this, but if it pleases the proj recs
del zelda
