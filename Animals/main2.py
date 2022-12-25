from zoo import *
from jiraf import *
from wolf import *

albert1 = Jiraf('Albert1', 10, 4, 15)
albert2 = Jiraf('Albert2', 10, 2, 15)
albert3 = Jiraf('Albert3', 10, 3, 15)
albert4 = Jiraf('Albert4', 10, 5, 15)
albert5 = Jiraf('Albert5', 10, 6, 15)

b1 = Wolf('jjfefe1', 32, 3, 8)
b2 = Wolf('jjfefe2', 32, 3, 8)
b3 = Wolf('jjfefe3', 32, 3, 8)
b4 = Wolf('jjfefe4', 32, 3, 8)

volier = Volier('вольер для жирафов', 'Савана', 45)
volier2 = Volier('вольер для волков', 'леса умеренных широт, тайга, тундра, степи и горные системы', 32)
volier3 = Volier('lkk','Савана',45)

zoo1 = Zoo('Зоопарк', [volier, volier2])

zoo1.addFoodInvoliers([volier, volier2], ['hh', 'qqq'])
zoo1.foodInAllmangers()
zoo1.addAnimalInvolier([albert1, albert2], volier)
zoo1.allAnimalsInZoo()
print(volier.EatFood(['морковка']))
print(volier.foodInManger)
zoo1.addVolier(volier3)
print(zoo1.allVoliers)
print(zoo1.removeAnimal(volier, albert1, volier3))
zoo1.allAnimalsInZoo()
zoo1.addAnimalInvolier([albert5, albert4], volier3)
zoo1.allAnimalsInZoo()
zoo1.neededFoodForAnimalsInVoliers()