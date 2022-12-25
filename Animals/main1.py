from jiraf import *
from wolf import *
from zoo import *

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

print(volier.allAnimals)
print(volier.sizeOfVolier)
volier.AddAnimal(albert1)
print(volier.allAnimals)
print(volier.sizeOfVolier)
volier.AddAnimal(albert1)
print(volier.allAnimals)
volier.AddAnimal(albert2)
print(volier.allAnimals)
print(volier.sizeOfVolier)

volier2.AddAnimal(b1)
volier2.AddAnimal(b2)
volier2.AddAnimal(b3)
volier2.AddAnimal(b4)

print(volier2.allAnimals)
print(volier.sizeOfVolier)

volier.KillAnimal(albert1)
print(volier.allAnimals)
print(volier.sizeOfVolier)
volier.KillAnimal(albert2)
print(volier.allAnimals)
print(volier.sizeOfVolier)
volier.AddAnimal(albert1)
volier.AddAnimal(albert2)
volier.EatFood(
    ['морковка', 'морковка', 'морковка', 'морковка', 'qqq', 'морковка', 'jjjj', 'морковка', 'морковка', 'морковка',
     'морковка',
     'морковка', 'морковка', 'морковка', 'морковка', 'морковка'])
volier.needFoodAnimal
print(volier.foodInManger)

volier2.AddAnimal(b1)

volier3 = Volier('lkk', 'Савана', 35)

zoo1 = Zoo("Зоопарк", [volier, volier2])

print(zoo1.allVoliers)
print(zoo1.removeAnimal(volier, albert1, volier2))
print(zoo1.removeAnimal(volier2, albert1, volier2))

zoo1.addVolier(volier3)
print(zoo1.allVoliers)

zoo1.allAnimalsInZoo()
zoo1.deleteVolier(volier)
print(zoo1.allVoliers)
volier3._addFoodInManger(['ppp', 'jjj'])
print(volier3.foodInManger)

zoo1.addFoodInvoliers([volier, volier3], ['морковка', 'морковка', 'морковка', 'морковка', 'морковка', 'hhh'])
zoo1.foodInAllmangers()
zoo1.addFoodInvoliers([volier, volier2], ['hhh', 'jjj'])
zoo1.foodInAllmangers()
