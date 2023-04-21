#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6410
#
# Created:     24/11/2022
# Copyright:   (c) TWY-6410 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Inventory check

def Exists(Item):
    Inventroy = 'Sword, Shield, Potion, Amulet'

    if Item in Inventroy:
        print('The item {} is in the players inventory.'.format(Item))
    else:
         print('The item {} is not in the players inventory.'.format(Item))

#Main
Exists(input('Item to check for: '))

