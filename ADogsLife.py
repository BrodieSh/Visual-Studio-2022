#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6410
#
# Created:     18/11/2022
# Copyright:   (c) TWY-6410 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DogsLife

#Subroutine
def HumToDog(Par1):
    if Par1 <= 2:
        return(Par1*12)
    elif Par1 > 2:
        return((24+(6*Par1))-2)

#Main#

print('The dog is {} years old in dog years'.format(HumToDog(float(input('How old is the dog in human years? ')))))