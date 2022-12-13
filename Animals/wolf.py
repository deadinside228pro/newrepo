from animal import *


class Wolf(Animal):
    def __init__(self, name, age, howmanyfoodeat, size):
        super().__init__(name, age, howmanyfoodeat, size, voice='авуууууу уав-уав', typeOfFood=['мясо', 'рыба', 'яйца'],
                         squad='хищное', habitat='леса умеренных широт, тайга, тундра, степи и горные системы',
                         species='волк обыкновенный')
