from animal import *


class Volier:
    def __init__(self, name, biom, size):
        self.__volier = []
        self.__name = name
        self.__biom = biom
        self.__size = size
        self.__manger = {}

    @property
    def allAnimals(self):
        animalsInVolier = []
        for i in self.__volier:
            i:Animal
            animalsInVolier.append(i.name)
        return animalsInVolier


    def AddAnimal(self, newanimal: Animal):
        if len(self.__volier) == 0 and self.__biom == newanimal.habitat:
            self.__size -= newanimal.size
            return self.__volier.append(newanimal)
        if newanimal in self.__volier:
            return "there is can not be two similar animals"
        if self.__biom != newanimal.habitat:
            return print('он здесь не уживётся')
        if self.__size < newanimal.size:
            return False
        if self.__biom == newanimal.habitat and self.__size >= newanimal.size:
            for i in self.__volier:
                i:Animal
                if i.squad == 'хищное' and i.species == newanimal.species:
                    self.__size -= newanimal.size
                    return self.__volier.append(newanimal)
                elif i.squad == 'травоядное':
                    self.__size -= newanimal.size
                    return self.__volier.append(newanimal)
        else:
            return print('он здесь не уживётся')


    def KillAnimal(self, animal):
        if animal in self.__volier:
            animal: Animal
            self.__size += animal.size
            return self.__volier.remove(animal)
        else:
            return False



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

    @property
    def sizeOfVolier(self):
        return self.__size

    @property
    def biomOfVolier(self):
        return self.__biom

    @property
    def nameOfVolier(self):
        return self.__name





        
        
