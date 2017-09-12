class Item(object):  # Parent class for items. Underutilized.
    """TODO: Consider moving make function here and removing subclassing in favor of a type variable
    used in the constructor"""

    def __init__(self, location):
        self.location = location
        self.icon = '?'  # Default icon
        self.item = True  # Flag for preventing creatures from being picked up

    def __str__(self):
        return self.icon


class Creature(object):  # Enemy creature
    # TODO: Add a unique(ish) name field
    # TODO: Creature behavior

    def __init__(self, location, health, damage):
        self.location = location
        self.health = health
        self.damage = damage
        self.icon = 'c'
        self.item = False

    def __str__(self):
        return self.icon


class Player(object):  # Player object.
    # TODO: Add stats

    def __init__(self):
        self.icon = '@'
        self.inv = {}
        self.health = 20
        self.item = False

    def __str__(self):
        return self.icon

    def show_inv(self):
        inv_text = "Your inventory consists of: "
        if not self.inv:
            inv_text = inv_text + "\nNothing."

        else:
            print("Your inventory consists of: ")
            for i in self.inv:
                inv_text += ("\n" + i)

        return inv_text


class Weapon(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items
    # TODO: Add damage range

    def __init__(self, location, damage):
        Item.__init__(self, location)
        self.damage = damage
        self.icon = 'w'


class Potion(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items

    def __init__(self, location, health_restored):
        Item.__init__(self, location)
        self.health_restored = health_restored
        self.icon = 'p'


class Room(object):
    # TODO: Establish order of icon preference

    def __init__(self, roomid):  # TODO: Remove roomid or make it relevant to anything
        self.contents = {}
        self.roomid = roomid
        self.icon = '.'  # Empty room icon, overriden by contents

    def __str__(self):  # Returns icon of first content over default icon.
        if not self.contents:
            return self.icon
        for i in self.contents:
            return str(self.contents[i])

        return str(self.roomid)

    def show(self):  # Displays the room contents.

        print("I am room: ", self.roomid)

        if not self.contents:
            print("I am an empty room")
        for i in self.contents:
            print(i)


class Dungeon(object):

    def __init__(self):

        self.map = {  # This is the current construction of the dungeon map.
            (1, 2): Room(1),
            (0, 1): Room(2),
            (1, 1): Room(3),
            (1, 0): Room(4),
            (2, 1): Room(5),
            (3, 1): Room(6),
            (4, 1): Room(7),
            (5, 1): Room(8),
            (6, 1): Room(9),
            (7, 1): Room(10),
            (5, 2): Room(11),
            (5, 3): Room(12),
            (5, 4): Room(13),
            (5, 5): Room(14),
            (5, 6): Room(15),
            (5, 7): Room(16),
            (5, 8): Room(17),
        }




        self.location = (1, 2)  # Starting location
        self.here = self.map[self.location]  # binds here to the current room. Used for most commands.
        self.here.contents['player'] = Player()  # Creates the player

        self.commandlist = {
            # Dictionary of first words of commands for directing the command parser to the proper function
            'take': self.take,
            'n': self.move,
            's': self.move,
            'w': self.move,
            'e': self.move,
            'make': self.make

                 }

        self.directions = {  # Mapping of cardinal directions for move function
            'n': ('north', 0, 1),
            's': ('south', 0, -1),
            'w': ('west', -1, 0),
            'e': ('east', 1, -0),
            'north': ('north', 0, 1),
            'south': ('south', 0, -1),
            'west': ('west', -1, 0),
            'east': ('east', 1, 0),
                }

    def show_map(self):  # Prints a crude map grid layout using # for empty rooms.
        for i in reversed(range(0, 32)):
            mapline = ""
            for j in range(0, 64):
                try:
                    # if (j, i) == self.location:
                    #     mapline += '@'
                    if self.map[(j, i)]:
                        mapline += str(self.map[(j, i)])
                except KeyError:
                    mapline += "#"
            print(mapline)

    def move(self, command):  # Simple movement. Hasn't generated two players yet.
        movement = self.directions[command[0]]
        try:
            self.map[(self.location[0] + movement[1], self.location[1] + movement[2])].contents['player'] = self.here.contents['player']
            del self.here.contents['player']
            self.here = self.map[(self.location[0] + movement[1], self.location[1] + movement[2])]
            self.location = (self.location[0] + movement[1], self.location[1] + movement[2])
            return "You move {}".format(movement[0])

        except KeyError:
            return "There is no exit in that direction"

    def make(self, command):  # TODO: Remove magic values, add *args for more dynamic creation
        try:
            if command[1] == 'potion':
                    if 'potion' not in self.here.contents:
                        self.here.contents['potion'] = Potion('potion', 20)
                        return "Created: Potion named {name} that heals {damage} health.".format(name='A potion', damage=20)
                    else:
                        print("Already a potion of that name here.")

            if command[1] == 'weapon':
                if 'weapon' not in self.here.contents:
                    self.here.contents['weapon'] = Weapon('weapon', 20)
                    return "Created: Weapon named {name} that deals {damage} damage.".format(name='A weapon', damage=20)
                else:
                    print("Already a weapon of that name here.")

            if command[1] == 'creature':
                if 'creature' not in self.here.contents:
                    self.here.contents['creature'] = Creature('creature', 20, 20)
                    return "Created: Creature named {name} that deals {damage} damage.".format(name='creature',health=20, damage=20)
                else:
                    print("Already a creature of that name here.")

        except IndexError:
            return "Failed to create an item due to index error"

    def attack(self, target): # TODO: Implement
        if target in self.here.contents:
            print(self.here.contents[target])

    def take(self, target):  # TODO: Rebuild input parameter to allow whitespace in item names, or write different take
        try:
            if not self.here.contents[target[1]].item:
                return "You cannot pick that up"
            self.here.contents['player'].inv[target[1]] = self.here.contents[target[1]]
            del self.here.contents[target[1]]

        except KeyError:
            return "There is no item with that name here."

    def command(self, answer):
        # Splits and case normalizes input. Matches first word to commandlist dict of bound functions. Strategy pattern?
        answer = answer.lower().split()
        try:
            return self.commandlist[answer[0]](answer)
        except KeyError:
            return "I didn't understand that"
