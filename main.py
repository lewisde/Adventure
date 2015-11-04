# David Lewis
# dlewis@olivetcollege.edu

from adventure.classes import Room
from adventure.classes import Item
from adventure.classes import Player

rear = Room('rear', {}, [], [])
kitchen = Room('kitchen', {}, [], [])
front = Room('front', {}, [], [])
attic = Room('attic', {}, [], [])
basement = Room('basement', {}, [], [])
bedroom = Room('bedroom', {}, [], [])

front.doors({'north': rear, 'west': kitchen})
rear.doors({'south': front, 'up': bedroom})
kitchen.doors({'east': front, 'down': basement, 'up': attic})
attic.doors({'down': kitchen})
basement.doors({'up': kitchen})
bedroom.doors({'down': rear})

# self, name, location, modifier, value, description, kind

knife = Item('knife', front, 50, 10, 'a pig sticker', 'weapon')
front.add_item(knife)
leather = Item('armor', front, 5, 10, 'leather', 'armor')
Item.skin = Item('skin', None, 0, 0, 'your epidermis', 'armor')
claws = Item('claws', front, 5, 10, 'a monster\'s', 'weapon')
table = Item('table', kitchen, 0, 0, 'a kitchen table', 'object')
kitchen.add_object(table)
bread = Item('bread', kitchen, 5, 2, 'stale bread', 'food')
kitchen.add_item(bread)

monster = Player('monster')
monster.weapon = claws
monster.location = front
monster.armor = leather

player = Player('player')
player.armor = Item.skin


def main():

    for character in Player.player_list:
        character.teleport()

    player.teleport()

    command_help()

    print(player.location)

    command = input('>>> ').lower().split()
    while not command:
        command = input('>>> ').lower().split()

    while command[0] != 'quit':
        if command[0] == 'look':
            print(player.location)
        elif command[0] == 'go':
            player.go_to(command)
        elif command[0] == 'help':
            command_help()
        elif command[0] == 'get':
            player.add_to_inventory(command)
        elif command[0] == 'drop':
            player.remove_from_inventory(command)
        elif command[0] == 'list':
            print(player)
        elif command[0] == 'teleport':
            player.teleport()
            print(player.location)
        elif command[0] == 'wield':
            player.wield(command)
        elif command[0] == 'wear':
            player.wear(command)
        elif command[0] == 'attack' or command[0] == 'kill':
            player.attack(command)
        elif command[0] == 'eat':
            player.eat(command)
        elif command[0] == 'drink':
            player.drink(command)
        elif command[0] == 'use':
            player.use(command)
        else:
            print('\nI don\'t understand you.\n')

        move_others()

        command = input('>>> ').lower().split()
        while not command:
            command = input('>>> ').lower().split()


def move_others():
    for creature in Player.player_list:
        if creature.name != 'player' and creature.location == player.location:
            print('\nFound you!\n')
            creature.attack(['attack', 'player'])
        elif creature.name != 'player':
            creature.teleport()


def command_help():
    print('\n\t\tCommands')
    print('\tlook\t\tgo <direction>')
    print('\tlist\t\tget <item>')
    print('\tteleport\tdrop <item>')
    print('\thelp\t\tattack/kill <monster>')
    print('\tquit\t\twield <weapon>')
    print('\t\t\twear <armor>')
    print('\t\t\tuse <item/object>')
    print('\t\t\teat <item>')
    print('\t\t\tdrink <item>')


if __name__ == '__main__':
    main()
