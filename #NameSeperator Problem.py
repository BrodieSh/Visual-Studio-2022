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


#NameSeperator Problem
#Subrotuine to find halves
def NameSep(FullName):
    FirstName = FullName[0:FullName.find(' ')]
    Surname = FullName[FullName.find(' '):len(FullName)]
    return('Firstname: {} \nSurname: {}'.format(FirstName, Surname))

#Execute
print(NameSep(input('Fullname: ')))