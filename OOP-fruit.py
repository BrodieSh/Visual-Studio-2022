class Fruit:
    def __init__(self,  Colour='None', Size='None',Taste='None'):
        self.Colour = Colour
        self.Size = Size
        self.Taste  = Taste
    
    def print_description(self):
        print(f'The fruit is {self.Colour} and is {self.Size} in size. It tastes {self.Taste}')
    
class Tropical(Fruit):
    def __init__(self,Colour,Size):
        super().__init__(Colour = Colour, Size = Size,Taste= 'Tropical')

class Citrus(Fruit):
    def __init__(self,Colour,Size,Bitter_Level):
        super().__init__(Colour = Colour, Size = Size, Taste= 'Bitter')
        self.Bitter_Level = Bitter_Level
    
    def print_description(self):
        print(f'The fruit is {self.Colour} and is {self.Size} in size. It tastes {self.Taste}. Its bitterness rating is {self.Bitter_Level}')
    
Mango = Tropical('Red','Medium')
Mango.print_description()
Lemon = Citrus('Yellow','Small',8)
Lemon.print_description()