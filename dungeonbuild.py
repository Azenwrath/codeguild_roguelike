# Dependent on lab_roguelike.py
import rogueclasses



def build_dungeon():
    dungeon = rogueclasses.Dungeon()
    # here = dungeon.map[1]
    # here.add_potion('Some place', 20)
    return dungeon


if __name__ == "__main__":
    build_dungeon()