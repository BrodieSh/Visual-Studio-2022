#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      TWY-6410
#
# Created:     10/03/2023
# Copyright:   (c) TWY-6410 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Human:
    def __init__(self, name='No name', age=0, nationality='None', gender='Jack'):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender

    def speak(self):
        print(f'Hello, my name is {self.name}.')

    def joke(self):
        print('Jack smells.')

bob = Human(name='Bob', age=57, nationality='Irish', gender='Masculine')
print("Object's Attributes:\n********************")
print(f'Name: {bob.name}\nAge: {bob.age}\nNationality: {bob.nationality}\nGender: {bob.gender}\n********************')
print('Object\'s Methods:\n********************')
bob.speak()

jack = Human(name='Jack Clayton', age=17, nationality='British/Polish', gender='Depends on the weather')
print("Object's Attributes:\n********************")
print(f'Name: {jack.name}\nAge: {jack.age}\nNationality: {jack.nationality}\nGender: {jack.gender}\n********************')
print('Object\'s Methods:\n********************')
jack.joke()