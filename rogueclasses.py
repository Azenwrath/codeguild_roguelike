class Item(object):  # Parent class for items
    def __init__(self, location):
        self.location = location


class Creature(object):
    # TODO: Add a unique(ish) name field
    icon = 'c'

    def __init__(self, location, health, damage):
        self.location = location
        self.health = health
        self.damage = damage

    def __str__(self):
        return self.icon
        #return "I am a creature in: %s. I have %i health. I am equipped with a %s" % (
        #self.location, self.health, self.damage)


class Weapon(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items
    icon = 'w'

    def __init__(self, location, damage):
        Item.__init__(self, location)
        self.damage = damage

    def __str__(self):
        return self.icon
        #return "I am a weapon in: %s, and I deal %i damage" % (self.location, self.damage)
        # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Potion(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items
    icon = 'p'

    def __init__(self, location, health_restored):
        Item.__init__(self, location)
        self.health_restored = health_restored

    def __str__(self):
        return self.icon
        #return "I am a potion in: %s, and I restore %i health" % (self.location, self.health_restored)
        # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Room(object):
    def __init__(self, roomid):  #TODO: Implement roomid
        self.contents = {}
        self.roomid = roomid
        #self.exits = exits
        pass

    def __str__(self):
        if not self.contents:
            return '_'
        for i in self.contents:
            return str(self.contents[i])


        return str(self.roomid)

    def add_potion(self, name , health_restored):
        try:
            if not self.contents[name]:
                self.contents[name] = (Potion(name, health_restored))
            else:
                print ("Already a potion of that name here.")
        except KeyError:
            self.contents[name] = (Potion(name, health_restored))


    def add_weapon(self, name, damage):
        #self.contents.append(Weapon(location, damage))
        try:
            if not self.contents[name]:
                self.contents[name] = (Weapon(name, damage))
            else:
                print ("Already a potion of that name here.")
        except KeyError:
            self.contents[name] = (Weapon(name, damage))

    def add_creature(self, name, health, damage):
        #self.contents.append(Creature(location, health, damage))
        try:
            if not self.contents[name]:
                self.contents[name] = (Creature(name, health, damage))
            else:
                print ("Already a potion of that name here.")
        except KeyError:
            self.contents[name] = (Creature(name, health, damage))





    def show(self):



        print("I am room: ", self.roomid)

        if not self.contents:
            print("I am an empty room")
        for i in self.contents:
            print(i)

    def show_exits(self):
        #output = ''
        #for i in self.exits.keys():
        #     output += str(i) + " "
        #print("Exits: ", output)
        pass


class Dungeon(object):

    # map = {
    #     1 : Room(1, {'south': 3}),
    #     2 : Room(2, {'east': 3}),
    #     3: Room(3, {'north': 3, 'west': 2, 'east': 4, 'south': 5}),
    #     4: Room(4, {'west': 3}),
    #     5: Room(5, {'north': 3}),
    # }

    map = {
        (1, 2): Room(1),
        (0, 1): Room(2),
        (1, 1): Room(3),
        (1, 0): Room(4),
        (2, 1): Room(5),
    }


    def __init__(self):
          # Starting location
        self.location = (1, 2)
        self.here = self.map[self.location]

    def show_map(self):
        for i in reversed(range(0, 6)):
            mapline = ""
            for j in range(0, 6):
                try:
                    if (j, i) == self.location:
                        mapline += '@'
                    elif self.map[(j, i)]:
                        mapline += str(self.map[(j, i)])
                except KeyError:
                    mapline += " "
            print(mapline)


    def move(self, direction):
        try:

            if direction == 'south':
                self.here = self.map[(self.location[0], self.location[1] -1)]
                self.location = (self.location[0], self.location[1] -1)
                print("I think I am at ", self.location, "and trying to go to ", (self.location[0], self.location[1] -1))
               # self.here = self.map[self.move(self.here.roomid, 'south')]
            if direction == 'north':
                self.here = self.map[(self.location[0], self.location[1] + 1)]
                self.location = (self.location[0], self.location[1] + 1)
                print("I think I am at ", self.location, "and trying to go to ",
                      (self.location[0], self.location[1] + 1))
                #self.here = self.map[self.move(self.here.roomid, 'north')]
            if direction == 'west':
                self.here = self.map[(self.location[0] - 1, self.location[1])]
                self.location = (self.location[0] - 1, self.location[1])
                print("I think I am at ", self.location, "and trying to go to ",
                      (self.location[0] - 1, self.location[1]))
                #self.here = self.map[self.move(self.here.roomid, 'west')]
            if direction == 'east':
                self.here = self.map[(self.location[0] + 1, self.location[1])]
                self.location = (self.location[0] + 1, self.location[1])
                print("I think I am at ", self.location, "and trying to go to ",
                      (self.location[0] + 1, self.location[1]))
                #self.here = self.map[self.move(self.here.roomid, 'east')]

            #return self.map[location].exits[direction]
        except KeyError:
            print("There is no exit in that direction")
            return

        except IndexError:
            print(self.location)
            print("There is no exit in that direction")
            return

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

            if answer[0] == 's':
                self.move('south')
            if answer[0] == 'n':
                self.move('north')
            if answer[0] == 'w':
                self.move('west')
            if answer[0] == 'e':
                self.move('east')


            if answer[0] == "make":
                if answer[1] == 'potion':
                    self.here.add_potion('A potion', 20)
                if answer[1] == 'weapon':
                    self.here.add_weapon('A weapon', 20)
                if answer[1] == 'creature':
                    self.here.add_creature('A creature', 20, 5)
            if answer[0] == 'attack':
                self.attack(answer[1])







        except ValueError:
            pass

        except IndexError:
            pass
