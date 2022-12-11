from animal import *


class Volier:
    def __init__(self, name, biom, size, squad, species):
        self.__volier = []
        self.__name = name
        self.__biom = biom
        self.__size = size
        self.__squad = squad
        self.__species = species
        self.__manger = []

    @property
    def allAnimals(self):
        l=[]
        for i in self.__volier:
            i:Animal
            l.append(i.name)
        return l


    def AddAnimal(self, newanimal: Animal):
        if self.__biom == newanimal.habitat and self.__size>newanimal.size and self.__squad == 'хищные' and self.__species == newanimal.species:
            self.__volier.append(newanimal)
            self.__size += newanimal.size
        elif self.__biom == newanimal.habitat and self.__size>newanimal.size and self.__squad == 'травоядное':
            self.__volier.append(newanimal)
            self.__size += newanimal.size
        else:
            print('он здесь не уживётся')


    def KillAnimal(self,animal):
        self.__volier.remove(animal)


    def EatFood(self,food=list):
        for k in food:
            self.__manger.append(k)
        for i in self.__volier:
            i:Animal
            for q in self.__manger:
                if i._EatenFood < i._Food:
                    if q in i._TypeOfFood:
                        i._EatenFood += 1
                        print(i._Name + ":", "хрямкс *жуёт* хрумск ")
                        self.__manger.remove(q)
                        self.__manger.insert(0,'')
                    elif q not in i._TypeOfFood:
                        print(i.name + ":","я такое не ем")
                else:
                    print(i.name + ":","я больше не буду")
                    break



    @property
    def foodInManger(self):
        return print(self.__manger)



    @property
    def needFoodAnimal(self):
        for i in self.__volier:
            i:Animal
            if i._EatenFood >= i._Food:
                i._IsFedded = True
                print(i.name + ':',i._IsFedded)
            else:
                print(i.name + ':',i._IsFedded,'мне нужно что-то из этого:',i._TypeOfFood)

    @property
    def doSound(self):
        for i in self.__volier:
            i:Animal
            i.voice

        
        
