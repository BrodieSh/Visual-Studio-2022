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

#City shortner

#Subroutine
def Cityyyy(City1,City2):

    if len(City1) < 4:
        Val1 = City1.upper()
    else:
        Val1 = City1[0:4].upper()
    if len(City2) < 4:
        Val2 = City2.upper()
    else:
        Val2 = City1[0:4].upper()


    print(Val1,'-', Val2)

Cityyyy(input('City one: '),input('City two: '))