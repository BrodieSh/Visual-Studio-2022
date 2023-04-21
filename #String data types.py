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

#String data types

#Subrotuine to concat name
def FullNam(String1,String2):
    return String1.upper() + " " + String2.upper()

#Main
Forename = 'John'
Surname = 'Smith'
Student = FullNam(Forename,Surname)
print('Full name: {}'.format(Student))