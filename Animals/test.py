from Jiraf import *
from main import *
from wolf import *
from Whitebear import *
from Hare import *

albert=Jiraf('Albert',10,2,8)
volier=Volier('вольер для жирафов','Савана',32,'травоядное','жираф')
volier.AddAnimal(albert)
print(volier.allAnimals)
b=Wolf('jjfefe',32,3,8)
volier.AddAnimal(b)
volier2=Volier('вольер для волков','леса умеренных широт, тайга, тундра, степи и горные системы',32,'хищные','волк обыкновенный')
volier2.AddAnimal(b)
print(volier2.allAnimals)
volier.doSound
volier2.doSound
volier.EatFood(['морковка','gafgaf','морковка','морковка'])
volier.foodInManger
volier.needFoodAnimal
robert=Hare('Robert',4,3,7)
volier.AddAnimal(robert)
print(volier.allAnimals)
volier.doSound
volier.EatFood(['груша','морковка','трава'])
volier.foodInManger
volier.needFoodAnimal






