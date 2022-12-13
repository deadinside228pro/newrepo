from animal import *


class Hare(Animal):
    def __init__(self, name, age, howmanyfoodeat, size):
        super().__init__(name, age, howmanyfoodeat, size, voice='fur-fur', typeOfFood=['капуста', 'трава', 'морковка'],
                         squad='травоядное', habitat='Савана', species='заяц')
