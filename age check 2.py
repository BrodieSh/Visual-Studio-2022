#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6410
#
# Created:     06/10/2022
# Copyright:   (c) TWY-6410 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Selection commands

#Subroutine to validate month

def ValidPreAge(Age):
    if Age >= 2 and Age <= 5:
        print('Child is eligable for preschool')
    else:
        print('Child is ineligable for preschool')

#Main execute
ValidPreAge(int(input('Enter child age: ')))