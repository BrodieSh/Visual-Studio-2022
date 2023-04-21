#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6410
#
# Created:     25/11/2022
# Copyright:   (c) TWY-6410 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#ASCII-EBCDIC

def Conv(Letter):
   Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

   if Alphabet.find(Letter) <= 8:
    Base = 193
    EBCDIC = Base +Alphabet.find(Letter)
   elif Alphabet.find(Letter) > 8 and Alphabet.find(Letter) <= 17:
        Base = 200
        EBCDIC = Base +Alphabet.find(Letter)
   elif Alphabet.find(Letter) > 17 and Alphabet.find(Letter) <= 26:
        Base = 208
        EBCDIC = Base +Alphabet.find(Letter)



   return('The ASCII value for the letter {} is {}. \n The EBCDIC value is {}.'.format(Letter,ord(Letter),EBCDIC))

#Exe
print(Conv(input('Letter:')))