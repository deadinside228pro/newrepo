from animal import *


class Hare(Animal):
    def __init__(self, name, age, howmanyfoodeat, size):
        super().__init__(name, age, howmanyfoodeat, size, voice='fur-fur', typeOfFood=['капуста', 'трава', 'морковка'],
                         squad='травоядное', habitat='леса, степи, лесостепи', species='заяц',foodVoice='хрум-хрум фыр-фыр хрум-хрум')
