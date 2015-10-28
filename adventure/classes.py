class Room:
    teleport_list = []

    def __init__(self, name, exits, items, objects):
        self.name = name
        self.exits = exits
        self.items = items
        self.objects = objects
        Room.teleport_list.append(self)

    def doors(self, outside):
        self.exits = outside

    def add_item(self, item):
        self.items.append(item)

    def add_object(self, thing):
        self.objects.append(thing)

    def __str__(self):
        output = '\nYou are in the {}.\n'.format(self.name)
        for char in Player.player_list:
            if char.name != 'player':
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
    item_list = []

    def __init__(self, name, location, damage, value, description):
        self.name = name
        self.location = location
        self.value = value
        self.description = description
        self.damage = damage
        Item.item_list.append(self)

    def __str__(self):
        output = '{}, {} - damage: {}, value: {} coin\n'.format(
            self.name,
            self.description,
            self.damage,
            self.value)
        return output

    def value(self):
        return self.value

    def examine(self):
        return self.description

    def drop(self, room):
        self.location = room


class Player:
    player_list = []

    def __init__(self, name):
        self.inventory = []
        self.health = 100
        self.weapon = None
        self.armor = None
        self.location = None
        self.name = name
        Player.player_list.append(self)

    def __str__(self):
        output = ''
        if self.inventory:
            for item in self.inventory:
                output += item.__str__()
        if self.weapon:
            output += '\nWielding: {} - {}\n'.format(
                self.weapon.name, self.weapon.description)
        if self.armor:
            output += '\nWearing: {} - {}\n'.format(
                self.armor.name, self.armor.description)
        if output:
            output = '\nInventory:\n' + output
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
        else:
            for item in self.location.objects:
                if command[1] == item.name:
                    print('\nYou can not carry that!\n')
            else:
                for item in self.location.items:
                    if command[1] == item.name:
                        self.inventory.append(item)
                        self.location.items.remove(item)
                        print('\nOkay.\n')
                        break
                else:
                    print('\nThere is no {} here!\n'.format(command[1]))

    def remove_from_inventory(self, command):
        if len(command) < 2:
            print('\nDrop what?\n')
        else:
            if self.weapon and command[1] == self.weapon.name:
                self.location.items.append(self.weapon)
                self.weapon = None
                print('\nOkay\n')
            elif self.armor and command[1] == self.armor.name:
                self.location.items.append(self.armor)
                # self.armor = mymap.skin
                print('\nOkay\n')
            else:
                for item in self.inventory:
                    if command[1] == item.name:
                        self.location.items.append(item)
                        self.inventory.remove(item)
                        print('\nOkay\n')
                        break
                else:
                    print('\nYou don\'t have that!\n')

    def wield(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
        else:
            for thing in self.inventory:
                if command[1] == thing.name:
                    self.weapon = thing
                    self.inventory.remove(thing)
                    print('\nYou are now wielding {}.\n'.format(
                        thing.description))
                    break
            else:
                print('\nYou don\'t have that!\n')

    def wear(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
        else:
            for item in self.inventory:
                if command[1] == item.name:
                    self.armor = item
                    self.inventory.remove(item)
                    print('\nYou are now wearing {}.\n'.format(item.name))
                    break
                else:
                    print('\nYou don\'t have that!\n')

    def attack(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        if not self.weapon:
            print('\nYou don\'t have a weapon!\n')
        else:
            for enemy in Player.player_list:
                if enemy.name == command[1] and \
                        enemy.location == self.location:
                    damage = self.weapon.damage - enemy.armor.damage
                    if damage > 0:
                        enemy.health -= damage
                    print('\n{} has been hit!\n'.format(enemy.name))
                    if enemy.health <= 0:
                        print('\nThe {} is dead!\n'.format(enemy.name))
                        if enemy.weapon:
                            self.location.items.append(enemy.weapon)
                        if enemy.armor:
                            self.location.items.append(enemy.armor)
                        for item in enemy.inventory:
                            self.location.items.append(item)
                        Player.player_list.remove(enemy)
                        print(self.location)
                    return
            else:
                print('\nThe {} isn\'t here!\n'.format(command[1]))