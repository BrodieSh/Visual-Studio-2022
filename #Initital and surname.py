#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6410
#
# Created:     21/11/2022
# Copyright:   (c) TWY-6410 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Initital and surname

#Subrotu
def InSur(Int1,Int2):
    Initial = Int1[0].upper()
    Surname = Int2.upper()
    return Initial, Surname

print(InSur(input('Forename: '),input('Surname: ')))