from classes import Room
from classes import Item
from classes import Player

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

knife = Item('knife', front, 20, 10, 'a pig sticker')
front.add_item(knife)

leather = Item('armor', front, 5, 10, 'leather')

claws = Item('claws', front, 5, 10, 'a monster\'s')

table = Item('table', kitchen, 0, 0, 'a kitchen table')
kitchen.add_object(table)

monster = Player('monster')
monster.weapon = claws
monster.location = front
monster.armor = leather

player = Player('player')
player.armor = leather

player_list = []
teleport_list = []
a = list(globals().values())
for item in a:
    if isinstance(item, Room):
        teleport_list.append(item)
    if isinstance(item, Player):
        player_list.append(item)


def move_others():
    for creature in player_list:
        if creature.name != 'player' and creature.location == player.location:
            print('\nFound you!\n')
            creature.attack(['attack', 'player'])
