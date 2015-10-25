import Adventure_map


class Room:

    exits = {}
    name = ''
    items = []
    objects = []

    def __init__(self, name, exits, items, objects):
        self.name = name
        self.exits = exits
        self.items = items
        self.objects = objects

    def doors(self, outside):
        self.exits = outside

    def add_item(self, item):
        self.items.append(item)

    def add_object(self, thing):
        self.objects.append(thing)

    def __str__(self):
        output = '\nYou are in the {}.\n'.format(self.name)
        for char in Adventure_map.player_list:
            if char.name != 'Player':
                if char.location.name == self.name:
                    output += '\nThere is a {} here!\n\n'.format(char.name)
        output += 'You can see exits: '
        for key in self.exits:
            output += '\n    {} ({})'.format(key, self.exits[key].name)
        if self.objects or self.items:
            output += '\n\nThe room contains:\n'
            if self.objects:
                for item in self.objects:
                    output += '    {}, {}\n'.format(
                        item.name, item.examine())
            if self.items:
                for item in self.items:
                    output += '    {}, {}\n'.format(
                        item.name, item.examine())
        else:
            output += '\n'
        return output


class Item:

    name = ''
    value = 0
    description = ''
    location = ''
    damage = 0

    def __init__(self, name, location, damage, value, description):
        self.name = name
        self.location = location
        self.value = value
        self.description = description
        self.damage = damage

    def __str__(self):
        output = 'name: {}, damage: {}, location: {}, value: {}, \
                  description: {}'.format(
            self.name,
            self.damage,
            self.location.name,
            self.value,
            self.description)
        return(output)

    def value(self):
        return(self.value)

    def examine(self):
        return(self.description)

    def drop(self, room):
        self.location = room


class Player:
    inventory = []
    health = 0
    weapon = 0
    armor = 0
    location = None
    name = 'Player'

    def __init__(self, name):
        self.inventory = []
        self.health = 100
        self.weapon = None
        self.armor = None
        self.location = None
        self.name = name

    def __str__(self):
        # output = '\n{}: {}, {}, {}, {}'.format(
        #     self.name, self.location, self.health, self.weapon, self.armor)
        output = ''
        if self.inventory:
            for item in self.inventory:
                output += '    {} - {}\n'.format(item.name, item.description)
        if self.weapon:
            output += 'Wielding: {} - {}\n'.format(
                self.weapon.name, self.weapon.description)
        if self.armor:
            output += 'Wearing: {} - {}\n'.format(
                self.armor.name, self.armor.description)
        if output:
            output = 'Inventory:\n' + output
        else:
            output = '\nYour pockets are empty.\n'
        return output

    def go_to(self, command):
        if len(command) > 1:
            if command[1] in self.location.exits.keys():
                self.location = self.location.exits[command[1]]
                print(self.location)
            else:
                print('\nYou can not go that way!\n')
        else:
            print('\nGo where?\n')

    def add_to_inventory(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        for item in self.location.objects:
            if command[1] == item.name:
                print('\nYou can not carry that!\n')
                return
        for item in self.location.items:
            if command[1] == item.name:
                self.inventory.append(item)
                self.location.items.remove(item)
                print('\nOkay.\n')
                return
        else:
            print('\nThere is no {} here!\n'.format(command[1]))
            return

    def remove_from_inventory(self, command):
        if len(command) < 2:
            print('\nDrop what?\n')
        else:
            if self.weapon and command[1] == self.weapon.name:
                self.location.items.append(self.weapon)
                self.weapon = None
                print('\nOkay\n')
                return
            else:
                for item in self.inventory:
                    if command[1] == item.name:
                        self.location.items.append(item)
                        self.inventory.remove(item)
                        print('\nOkay\n')
                        return
                else:
                    print('\nYou don\'t have that!\n')

    def wield(self, item):
        for thing in self.inventory:
            if item == thing.name:
                self.weapon = thing
                self.inventory.remove(thing)
                print('\nYou are nw wielding {}.\n'.format(thing.description))
                return
        else:
            print('\nYou don\'t have that!\n')

    def wear(self, item):
        if item in self.inventory:
            self.armor = item
            self.inventory.remove(item)
        else:
            print('\nYou don\'t have that!\n')

    def attack(self, monster):
        if not self.weapon:
            print('You don\'t have a weapon!\n')
        else:
            for enemy in Adventure_map.player_list:
                if enemy.name == monster and enemy.location == self.location:
                    damage = self.weapon.damage - enemy.armor.damage
                    if damage > 0:
                        enemy.health -= damage
                    print('\n{} has been hit!\n'.format(enemy.name))
                    if enemy.health <= 0:
                        print('The {} is dead!'.format(enemy.name))
                        if enemy.weapon:
                            self.location.items.append(enemy.weapon)
                        if enemy.armor:
                            self.location.items.append(enemy.armor)
                        for item in enemy.inventory:
                            self.location.items.append(item)
                        Adventure_map.player_list.remove(enemy)
                        print(self.location)
                    return
            else:
                print('\nThe {} isn\'t here!\n'.format(monster.name))
