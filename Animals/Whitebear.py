from animal import *
class Whitebear(Animal):
    def __init__(self,name,age,howmanyfoodeat,size):
        super().__init__(name,age,howmanyfoodeat,size,voice='roar',typeOfFood=['мясо','рыба','ягоды'],squad='хищные',habitat='Тундра',species='белый медведь')



