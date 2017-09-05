class Item(object):  # Parent class for items

    def __init__(self, location):
        self.location = location
        self.icon = '?'
        self.item = True

    def __str__(self):
        return self.icon


class Creature(object):
    # TODO: Add a unique(ish) name field


    def __init__(self, location, health, damage):
        self.location = location
        self.health = health
        self.damage = damage
        self.icon = 'c'
        self.item = False

    def __str__(self):
        return self.icon
        # return "I am a creature in: %s. I have %i health. I am equipped with a %s" % (
        # self.location, self.health, self.damage)


class Player(object):
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


    def __init__(self, location, damage):
        Item.__init__(self, location)
        self.damage = damage
        self.icon = 'w'

        # def __str__(self):
        #     return self.icon
        #     #return "I am a weapon in: %s, and I deal %i damage" % (self.location, self.damage)
        #     # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Potion(Item):
    # TODO Add a unique(ish) name field
    # TODO Distinguish between identified and unidentified items


    def __init__(self, location, health_restored):
        Item.__init__(self, location)
        self.health_restored = health_restored
        self.icon = 'p'
        #
        # def __str__(self):
        #     return self.icon
        # return "I am a potion in: %s, and I restore %i health" % (self.location, self.health_restored)
        # ""I am a potion in: ", self.location, " I restore: ", self.health_restored)


class Room(object):
    def __init__(self, roomid):  # TODO: Implement roomid
        self.contents = {}
        self.roomid = roomid
        # self.exits = exits
        pass

    def __str__(self):
        if not self.contents:
            return '.'
        for i in self.contents:
            return str(self.contents[i])

        return str(self.roomid)

    def add_potion(self, name, health_restored):
        try:
            if not self.contents[name]:
                self.contents[name] = (Potion(name, health_restored))
                return f"Created: Potion named {name} that heals {damage} health."
            else:
                print("Already a potion of that name here.")
        except KeyError:
            self.contents[name] = (Potion(name, health_restored))
            return f"Created: Potion named {name} that heals {damage} health."

    def add_weapon(self, name, damage):
        # self.contents.append(Weapon(location, damage))
        try:
            if not self.contents[name]:
                self.contents[name] = (Weapon(name, damage))
                return "Made weapon"  # f"Created: Weapon named{name} that deals {damage} damage."
            else:
                print("Already a weapon of that name here.")
        except KeyError:
            self.contents[name] = (Weapon(name, damage))
            return f"Created: Weapon named {name} that deals {damage} damage."

    def add_creature(self, name, health, damage):
        # self.contents.append(Creature(location, health, damage))
        try:
            if not self.contents[name]:
                self.contents[name] = (Creature(name, health, damage))
                return f"Created: Creature named {name} that has {health} health and deals {damage} damage."
            else:
                print("Already a creature of that name here.")

        except KeyError:
            self.contents[name] = (Creature(name, health, damage))
            return f"Created: Creature named {name} that has {health} health and deals {damage} damage."

    def show(self):

        print("I am room: ", self.roomid)

        if not self.contents:
            print("I am an empty room")
        for i in self.contents:
            print(i)

    def show_exits(self):
        # output = ''
        # for i in self.exits.keys():
        #     output += str(i) + " "
        # print("Exits: ", output)
        pass


class Dungeon(object):
    # map = {
    #     1 : Room(1, {'south': 3}),
    #     2 : Room(2, {'east': 3}),
    #     3: Room(3, {'north': 3, 'west': 2, 'east': 4, 'south': 5}),
    #     4: Room(4, {'west': 3}),
    #     5: Room(5, {'north': 3}),
    # }

    map = {  # This is the current construction of the dungeon map.
             # TODO: Move to __init__ and keep as an instance variable to allow multiple floors
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
    #
    #
    # commandlist = { # Dictionary of first words of commands for directing the command parser to the proper function
    #     'take': self.take,
    #     'n': self.move,
    #     's': self.move,
    #     'w': self.move,
    #     'e': self.move
    #         }



    def __init__(self):
        # Starting location
        self.location = (1, 2)
        self.here = self.map[self.location]
        self.here.contents['player'] = Player()

        self.commandlist = {  # Dictionary of first words of commands for directing the command parser to the proper function
            'take': self.take,
            'n': self.move,
            's': self.move,
            'w': self.move,
            'e': self.move
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

    def show_map(self):
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

    def move(self, command): # TODO: Reconstruct move functions based on updated command parser
        movement = self.directions[command[0]]
        try:
            self.map[(self.location[0] + movement[1], self.location[1] + movement[2])].contents['player'] = self.here.contents['player']
            del self.here.contents['player']
            self.here = self.map[(self.location[0] + movement[1], self.location[1] + movement[2])]
            self.location = (self.location[0] + movement[1], self.location[1] + movement[2])
            return "You move {}".format(movement[0])


        except KeyError:
            return "There is no exit in that direction"



    # def move(self, direction):
    #     try:
    #
    #         if direction == 'south':
    #             # print("Pre move: ", self.map[(self.location[0], self.location[1] - 1)].contents['player'])
    #             self.map[(self.location[0], self.location[1] - 1)].contents['player'] = self.here.contents['player']
    #             del self.here.contents['player']
    #             # self.here.contents['player']
    #             # print("Post move: ",self.map[(self.location[0], self.location[1] - 1)].contents['player'])
    #             self.here = self.map[(self.location[0], self.location[1] - 1)]
    #             self.location = (self.location[0], self.location[1] - 1)
    #
    #             return "You move south"
    #             # self.here = self.map[self.move(self.here.roomid, 'south')]
    #         if direction == 'north':
    #             self.map[(self.location[0], self.location[1] + 1)].contents['player'] = self.here.contents['player']
    #             del self.here.contents['player']
    #
    #             self.here = self.map[(self.location[0], self.location[1] + 1)]
    #             self.location = (self.location[0], self.location[1] + 1)
    #             return "You move north"
    #             # self.here = self.map[self.move(self.here.roomid, 'north')]
    #         if direction == 'west':
    #             self.map[(self.location[0] - 1, self.location[1])].contents['player'] = self.here.contents['player']
    #             del self.here.contents['player']
    #
    #             self.here = self.map[(self.location[0] - 1, self.location[1])]
    #             self.location = (self.location[0] - 1, self.location[1])
    #             return "You move west"
    #             # self.here = self.map[self.move(self.here.roomid, 'west')]
    #         if direction == 'east':
    #             self.map[(self.location[0] + 1, self.location[1])].contents['player'] = self.here.contents['player']
    #             del self.here.contents['player']
    #
    #             self.here = self.map[(self.location[0] + 1, self.location[1])]
    #             self.location = (self.location[0] + 1, self.location[1])
    #             return "You move east"
    #             # self.here = self.map[self.move(self.here.roomid, 'east')]
    #
    #             # return self.map[location].exits[direction]
    #     except KeyError:
    #         print("There is no exit in that direction")
    #         return
    #
    #     except IndexError:
    #         print(self.location)
    #         print("There is no exit in that direction")
    #         return

    def menu(self):
        print('''
        go [direction]
        
        ''')

    def attack(self, target):
        if target in self.here.contents:
            print(self.here.contents[target])

    def take(self, target):
        try:
            if not self.here.contents[target].item:
                return "You cannot pick that up"
            self.here.contents['player'].inv[target] = self.here.contents[target]
            del self.here.contents[target]

        except KeyError:
            return "There is no item with that name here."

    def command(self, answer): # TODO: Parse the input and make separate dicts for one word and two word commands

                # TODO: Idea: Make wrapper functions for single word commands that point to a dict in a TypeError to eliminate the need to check for words in any two word occurence

        answer = answer.lower().split()
        return self.commandlist[answer[0]](answer)




        # commandlist = {
        #     'take': self.take,
        #     'n': (self.move, 'north'),
        #     's': self.move('south'),
        #     'w': self.move('west'),
        #     'e': self.move('east')
        #     }
        #




# if first_pick == 'n':
#     return self.move('north')
# if first_pick == 'w':
#     return self.move('west')
# if first_pick == 'e':
#     return self.move('east')




#
# if first_pick == "make": TODO: Add to new parser, merge make functions
#     if answer[1] == 'potion':
#         return self.here.add_potion('potion', 20)
#     if answer[1] == 'weapon':
#         return self.here.add_weapon('weapon', 20)
#     if answer[1] == 'creature':
#         return self.here.add_creature('creature', 20, 5)
# if first_pick == 'attack':
#     self.attack(answer[1])
#
# if first_pick == "inv": TODO: Add to new parser
#     return self.here.contents['player'].show_inv()
#
# if first_pick == "take": TODO: Add to new parser
#     return self.take(answer[1])

# try:
#     if not self.here.contents[answer[1]].item:
#         return "You cannot pick that up"
#     self.here.contents['player'].inv[answer[1]] = self.here.contents[answer[1]]
#     del self.here.contents[answer[1]]
#
# except KeyError:
#     return "There is no item with that name here."
