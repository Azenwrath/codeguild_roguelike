class Item(object):  # Parent class for items
    def __init__(self, location):
        self.location = location


class Creature(object):
    # TODO: Add a unique(ish) name field


    def __init__(self, location, health, damage):
        self.location = location
        self.health = health
        self.damage = damage

    def __str__(self):
        return "I am a creature in: %s. I have %i health. I am equipped with a %s" % (
        self.location, self.health, self.damage)


class Weapon(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items

    def __init__(self, location, damage):
        Item.__init__(self, location)
        self.damage = damage

    def __str__(self):
        return "I am a weapon in: %s, and I deal %i damage" % (self.location, self.damage)
        # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Potion(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items

    def __init__(self, location, health_restored):
        Item.__init__(self, location)
        self.health_restored = health_restored

    def __str__(self):
        return "I am a potion in: %s, and I restore %i health" % (self.location, self.health_restored)
        # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Room(object):
    def __init__(self, roomid, exits):  #TODO: Implement roomid
        self.contents = {}
        self.roomid = roomid
        self.exits = exits
        pass

    def add_potion(self, name , health_restored):
        try:
            if not self.contents[name]:
                self.contents[name] = (Potion(name, health_restored))
            else:
                print ("Already a potion of that name here.")
        except KeyError:
            self.contents[name] = (Potion(name, health_restored))


    def add_weapon(self, location, damage):
        self.contents.append(Weapon(location, damage))

    def add_creature(self, location, health, damage):
        self.contents.append(Creature(location, health, damage))

    def show(self):
        print("I am room: ", self.roomid)

        if not self.contents:
            print("I am an empty room")
        for i in self.contents:
            print(i)

    def show_exits(self):
        output = ''
        for i in self.exits.keys():
            output += str(i) + " "
        print("Exits: ", output)


class Dungeon(object):

    map = {
        1 : Room(1, {'south': 3}),
        2 : Room(2, {'east': 3}),
        3: Room(3, {'north': 3, 'west': 2, 'east': 4, 'south': 5}),
        4: Room(4, {'west': 3}),
        5: Room(5, {'north': 3}),
    }

    def __init__(self):
        self.here = self.map[1]  # Starting location

    def move(self, location, direction):
        try:
            return self.map[location].exits[direction]
        except:
            print("There is no exit in that direction")
            return location

    def menu(self):
        print('''
        go [direction]
        
        ''')

    def attack(self, target):
        if target in self.here.contents:
            print(self.here.contents[target])

    def command(self, answer):
        try:

            answer = answer.lower().split()

            if answer[0] == 'go':
                self.here = self.map[self.move(self.here.roomid, answer[1])]
            if answer[0] == 's':
                self.here = self.map[self.move(self.here.roomid, 'south')]
            if answer[0] == 'n':
                self.here = self.map[self.move(self.here.roomid, 'north')]
            if answer[0] == 'w':
                self.here = self.map[self.move(self.here.roomid, 'west')]
            if answer[0] == 'e':
                self.here = self.map[self.move(self.here.roomid, 'east')]


            if answer[0] == "make":
                if answer[1] == 'potion':
                    self.here.add_potion('meh', 20)
                if answer[1] == 'weapon':
                    self.here.add_weapon('meh', 20)
                if answer[1] == 'creature':
                    self.here.add_creature('meh', 20, 5)
            if answer[0] == 'attack':
                self.attack(answer[1])







        except ValueError:
            pass

