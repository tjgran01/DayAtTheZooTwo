# Day At The Zoo Two:

Here is an implimentation of the DayAtTheZoo program, but written in Python 3.6.
As such, you'll need at least Python 3.6 to run the thing! That can be downloaded
here.

No external packages were used in the development of this program, but in case
there are some issues - a `requirements.txt` file can be found in this directory.

To install that stuff - open up a terminal (or cmd for Windows), andddd.

`$ git clone https://github.com/tjgran01/DayAtTheZooTwo.git`

Move into the repo.

`$ cd DayAtTheZooTwo`

create a python3.x (.6 or .7 should work) virtual environment and activate the environment.

`$ python3.{x} -m venv venv`

`$ source venv/bin/activate` (For MacOS / Linux)

`$ .\venv\bin\activate.bat` (Windows)

Then install requirements.

`$ pip install -r requirements.txt`


## Documentation Here:

*Note: The requirements for the adaptations for project 2 are* **in bold** *within the text below*

### ZooKeeper.py

The `Zooset_wake_behaviorsKeeper()` class is currently in this file. The `ZooKeeper()` is **an observable** that is responsible for taking care of all of the animals in
the zoo. The `ZooKeeper()` has a name, and an optional boolean argument to run the day at the zoo program (`run_day_at_zoo`), which is set to `False` by default.

 The `ZooKeeper()` first uses the `AnimalFactory()` class to instantiate a list of `Animal()` objects under his/her supervision.

 The `ZooKeeper()` wakes up in the morning (this behavior is delegated to the `WakeUpBehavior()` class, using **the strategy pattern**, as animals also use this behavior), and has the methods available to take care of the animals throughout the day.

### ZooAnnouncer.py

This file contains the ZooAnnouncer() class. The class is **an observer** of the
ZooKeeper() class. This Whenever the ZooKeeper() broadcasts a message out, the ZooAnnouncer object can
format the message and print it to the console.

### Animal.py

Every animal class is included within this file (at all levels of inheritance). There is a behavior included in each level of inheritance for all animal classes. The `Animal()` superclass delegates one of it's behaviors to the `WakeUpBehavior()` class, using **the strategy pattern**.

### AnimalFactory.py

The `AnimalFactory()` class lives in this file. This class is able to instantiate object instances of the `Animal()` class. There is also a method (`set_wake_behaviors()`) that can set the wake_behavior of each `Animal()` object passed to it.


## Project Requirements (Original):

Write a simple OO program in Java 8 or later that implements a Zoo full of Animals.  The Animals in
your Zoo are represented on slide 16 of Lecture 5.  Create a class structure similar to slide 17 with at
least three levels of inheritance (e.g. Animal, Feline, Cat).  You may decide how many of each animal live
in your zoo, but there should be at least two instances of each subclass (like Cat).  Individual animals
should have individual names for their instances that start with the same letter of their subclass (e.g.
Charlie and Chloe for Cat).  

You will also need a class for a Zookeeper.  The Zookeeper will have the following responsibilities – wake
the animals, roll call the animals, feed the animals, exercise the animals, shut down the zoo.  Each
animal will have a method that responds to this (wakeup, make noise, eat, roam, sleep).  You can decide
when it’s appropriate to use a method at a superclass or subclass level for each animal’s behavior, but
there should be some behaviors that are placed at each of the three inheritance levels.  In at least one
case (probably for the Cats) use a random number generation to select from alternative responses to
animal actions.

When the program runs, the Zookeeper should execute each of his responsibilities in order (display a
string for each action he executes), and the animals should respond by displaying strings with their
name, their type, and their response to the Zookeeper.  It is likely you will have a main program that
instantiates the objects before they begin to act.  Your program should demonstrate polymorphism by
asking your collection of animals to perform their tasks by referring to a collection of all animals at the
Zoo when executing methods.  Capture the text output of the final program in an out file called 'datatthezoo.out'.

## Project Requirements (New):

Recall from Project 1 the OO program you or your team wrote in Java 8 or later that implements a Zoo
full of Animals.  Using that code and its original requirements as a basis (see the previous assignment
details if needed), perform the following tasks:

a) Completely rewrite the program in another OO language of your choice; any OO language other than
Java.  The only requirement is that the language does have clear OO support (so, not C or FORTRAN, for
instance).
b) Add at least one implementation of the strategy pattern by having at least one Animal behavior
delegated and referenced by Animals rather than being inherited and overridden.  This means when
Animals are instantiated, the behavior they need will have to be initialized for them in a strategy pattern
manner.  Clearly document in the code where the strategy pattern is applied.

c) Add an implementation of the observer pattern.  Create a new observer class called the
ZooAnnouncer.  At the start of the program, the ZooAnnouncer will observe the ZooKeeper, which will
be modified to be observable.  When the ZooKeeper is starting to perform one of their tasks, they will
create an observable event for the ZooAnnouncer.  The ZooAnnouncer will respond to this by telling the
Zoo (issuing a print statement) something like “Hi, this is the Zoo Announcer.  The Zookeeper is about to
wake the animals!”.  (Note, this should not replace the text messages the ZooKeeper themselves may
issue from the original flow.)  Once the ZooKeeper completes his last task for the day, the ZooAnnouncer
should cease observing and deconstruct.  Clearly document in the code where the observer pattern is
applied.

Code should be clearly designed in an OO fashion throughout and should be clearly documented.  
Output from the program should be captured and provided as in Project 1.
