# Adventure

This is a functional test bed used to demostrate the efficacy of objects to my Python class.

There are three classes: Room, Item, and Player. Instances of classes are referenced by their name property.

Rooms began with names and exits, exits being a dictionary of other rooms, the keys of which match player input commands. This results in a room node graph with exit edges. Currently there is no cost. Even when added, path-finding should be an easy addition. 

Items and objects differ in that objects are not interactable. Items can be picked up, dropped, and wielded or worn. 

Players have inventory, health, and the ability to fight. Currently, monsters are of the player class and don't move. This can be changed in the move_others() function.

All instances can be printed to show their contents through look (Rooms) and list(Players). Items show in either case.

This was a fun exercise. I will add functionality as ideas come.

## Commands

go {'north', 'south', 'east', 'west', 'up', 'down'} - Directions are based on the current map. They are customizable during room instantiation.

look - displays room contents

get *item* - Transfers item from room inventory to player inventory

drop *item* - Removes item from from player inventory

attack/kill *monster* - Damages monster based on weapon and armor modifiers

wield *weapon* - Transfers weapon from player inventory to player hand

wear *armor* - Transfers armor from player inventory to player body

teleport - Places player in a pseudo-randomly chosen room.

use - 

eat -

drink -

help - Displays list of commands

quit - Quits game