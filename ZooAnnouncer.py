class ZooAnnouncer():
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

        print("-!" * 20)
        print(f"ZoOaNnOuNcEr hErE!: {self.make_typeface_annoying(event)}")
        print("-!" * 20)
