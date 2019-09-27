class ZooAnnouncer():
    """
    ZooAnnouncer() object is an observer of ZooKeeper(). Whenever the
    ZooKeeper() broadcasts a message out, the ZooAnnouncer object can
    format the message and print it to the console.
    """
    def __init__(self, name="Zelda"):
        self.name = name
        self.announce(f"Zookeeper {self.name} here! Enjoy the Zoo!")


    def make_typeface_annoying(self, announcement):
        """MaKeS ThInGs lOoK LiKe ThIs."""

        new_str = []
        for i, char in enumerate(announcement):
            if i % 2 == 0:
                new_str.append(char.upper())
            else:
                new_str.append(char)

        return "".join(new_str)


    def announce(self, event):
        """Prints a message from the ZoOaNnOuNcEr"""

        print("-!" * 20)
        print(f"ZoOaNnOuNcEr hErE!: {self.make_typeface_annoying(event)}")
        print("-!" * 20)
