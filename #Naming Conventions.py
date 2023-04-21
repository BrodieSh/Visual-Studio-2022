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

#Naming Conventions

#Subroutine
def NameConvention(Par1,Par2,Conv):
    if Conv == 'kebab-case':
        return('{}-{}'.format(Par1.lower(),Par2.lower()))
    elif Conv == 'snake_case':
        return('{}_{}'.format(Par1.lower(),Par2.lower()))
    elif Conv == 'camelCase':
        return('{}{}'.format((Par1.lower()),Par2[0].upper()+Par2[1:len(Par2)].lower()))
    elif Conv == 'PascalCase':
        return('{}{}'.format(Par1[0].upper()+Par1[1:len(Par1)].lower(),Par2[0].upper()+Par2[1:len(Par2)].lower()))
    else: return('Invalid Convention')

#Execute
print(NameConvention(input('Identifier one:'),input('Identifier two:'),input('Naming convention:')))