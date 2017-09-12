import unittest
from . import rogueclasses



class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room = rogueclasses.Room(1)

    def test_icon(self):
        self.assertEqual(self.room.icon, '.')

    def test_room_inv(self):
        self.room.contents['weapon']= rogueclasses.Weapon('here', 25)
        self.assertEqual(len(self.room.contents), 1)




class TestParser(unittest.TestCase):
    def setUp(self):
        self.map = rogueclasses.Dungeon()


    def test_move(self):
        self.assertEqual(self.map.location, (1, 2))
        self.map.command("s")
        self.assertEqual(self.map.location, (1, 1))

    def test_make(self):
        self.map.command('make potion')
        self.map.command('make weapon')
        self.assertEqual(len(self.map.here.contents), 3)


class TestItems(unittest.TestCase):
    def setUp(self):
        self.potname, self.weapname = 'A potion', 'A weapon'
        self.potvalue, self.weapvalue = 20, 20

        self.potion = rogueclasses.Potion(self.potname, self.potvalue)
        self.weapon = rogueclasses.Weapon(self.weapname, self.weapvalue)

    def test_potion(self):
        self.assertEqual(self.potion.health_restored, self.potvalue)
        self.assertEqual(self.potion.location, self.potname)

class TestCreatures(unittest.TestCase):
    def setUp(self):
        self.creatureloc = 'Here'
        self.creaturehp = 20
        self.creaturedmg = 30

        self.creature = rogueclasses.Creature(self.creatureloc, self.creaturehp, self.creaturedmg)

    def test_creature(self):
        self.assertEqual(self.creature.location, self.creatureloc)
        self.assertEqual(self.creature.health, self.creaturehp)
        self.assertEqual(self.creature.damage, self.creaturedmg)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = rogueclasses.Player()

    def test_inv(self):
        self.assertEqual(self.player.inv, {})
        self.player.inv['weapon'] = rogueclasses.Weapon('Sword', 20)
        self.player.inv['potion'] = rogueclasses.Potion('Potion', 20)

        self.assertIn('weapon', self.player.inv)
        self.assertIn('potion', self.player.inv)

    def test_take(self):
        self.here = rogueclasses.Dungeon()
        self.here.command('make potion')
        self.here.command('take potion')
        self.assertIn('potion', self.here.here.contents['player'].inv)
