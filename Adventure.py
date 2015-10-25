# David Lewis
# dlewis@olivetcollege.edu

import random
import Adventure_map


def main():
    player = Adventure_map.player
    # for character in Adventure_map.player_list:
    #     teleport(character)

    # teleport(player)
    player.location = Adventure_map.front

    print(command_help())

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
            print(command_help())
        elif command[0] == 'get':
            player.add_to_inventory(command)
        elif command[0] == 'drop':
            player.remove_from_inventory(command)
        elif command[0] == 'list':
            print(player)
        elif command[0] == 'teleport':
            teleport(player)
            print(player.location)
        elif command[0] == 'wield':
            player.wield(command[1])
        elif command[0] == 'wear':
            player.wear(command[1])
        elif command[0] == 'attack' or command[0] == 'kill':
            player.attack(command[1])
        else:
            print('\nI don\'t understand you.\n')

        Adventure_map.move_others()

        command = input('>>> ').lower().split()
        while not command:
            command = input('>>> ').lower().split()


def teleport(player):
    teleport_list = Adventure_map.teleport_list
    next = random.choice(range(len(teleport_list)))
    player.location = teleport_list[next]


def command_help():
    output = '\n\nCommands: go, look, get, drop, attack, kill, wield, wear,'
    output += ' help, teleport, and quit.\n'
    return output

if __name__ == '__main__':
    main()
