# Adventure

This is a functional test bed used to demostrate the efficacy of objects to my Python class.

There are three classes: Room, Item, and Player. Instances of classes are referenced by their name property.

Rooms began with names and exits, exits being a dictionary of other rooms, the keys of which match player input commands. This results in a room node graph with exit edges. Currently there is no cost. Even when added, path-finding should be an easy addition. 

Items and objects differ in that objects are not interactable. Items can be picked up, dropped, and wielded or worn. 

Players have inventory, health, and the ability to fight. Currently, monsters are of the player class and don't move. This can be changed in the move_others() function.

All instances can be printed to show their contents through look (Rooms) and list(Players). Items show in either case.

This was a fun exercise. I will add functionality as ideas come.