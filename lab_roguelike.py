from dungeonbuild import *
dungeon = build_dungeon()

here = dungeon.map[(1,2)]
#here = Room(1)
prompt = "Welcome to PDX Code Guild Rogue Lab!"
while True:
    try:

        dungeon.show_map()
        dungeon.here.show_exits()
        dungeon.here.show()
        print("Prompt: ", prompt)
        print()
        prompt = dungeon.command(input("Please enter a command: "))

        # menu = input('''
        #         Choose an option
        #         1 -- Make a potion
        #         2 -- Make a weapon
        #         3 -- Make a creature
        #         4 -- List the contents of the room
        #         5 -- Move a direction
        #         x -- Exit
        #         20/20: ''')
        # if menu == '1':
        #     here.add_potion('Some place', 20)
        #
        # elif menu == '2':
        #     here.add_weapon('At a place', 5)
        # elif menu == '3':
        #     here.add_creature('Dungeontown', 20, 20)
        # elif menu == '4':
        #     here.show()
        # elif menu == '5':
        #     dungeon.command(input("Please enter a direction to move"))
        #     # newroom = dungeon.move(here.roomid, input('Enter a direction to move: '))
        #     # here = dungeon.map[newroom]
        # elif menu == 'x':
        #     exit()

    except ValueError:
        pass
