from dungeonbuild import *
dungeon = build_dungeon()

here = dungeon.map[(1,2)]
#here = Room(1)
prompt = "Welcome to PDX Code Guild Rogue Lab!"
while True:
    try:

        dungeon.show_map()

        dungeon.here.show()
        print("Prompt: ", prompt)
        print()
        prompt = dungeon.command(input("Please enter a command: "))


    except ValueError:
        pass
