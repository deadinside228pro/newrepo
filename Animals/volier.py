from animal import *


class Volier:
    def __init__(self, name, biom, size):
        self.__volier = []
        self.__name = name
        self.__biom = biom
        self.__size = size
        self.__manger = []
        self.__conuntOfFoodInManger = 0

    @property
    def allAnimals(self):
        animalsInVolier = []
        for i in self.__volier:
            i: Animal
            animalsInVolier.append(i.name)
        return animalsInVolier

    def AddAnimal(self, animal_new: Animal):
        if len(self.__volier) == 0 and self.__biom == animal_new.habitat:
            self.__size -= animal_new.size
            return self.__volier.append(animal_new)
        if animal_new in self.__volier:
            return "there is can not be two similar animals"
        if self.__biom != animal_new.habitat:
            print('он здесь не уживётся')
            return
        if self.__size < animal_new.size:
            return False
        if self.__biom == animal_new.habitat and self.__size >= animal_new.size:
            for i in self.__volier:
                i: Animal
                if i.squad == 'хищное' and i.species == animal_new.species:
                    self.__size -= animal_new.size
                    return self.__volier.append(animal_new)
                elif i.squad == 'травоядное':
                    self.__size -= animal_new.size
                    return self.__volier.append(animal_new)
        else:
            print('он здесь не уживётся')
            return

    def KillAnimal(self, animal):
        if animal in self.__volier:
            animal: Animal
            self.__size += animal.size
            return self.__volier.remove(animal)
        else:
            return False

    def EatFood(self, food1: list):
        if type(food1) != list:
            print('передай, пожалуйста, лист с едой')
            return
        for k in food1:
            self.__manger.append(k)
            self.__conuntOfFoodInManger += 1
        if self.__conuntOfFoodInManger == 0:
            print('кормушка пуста')
            return
        elif self.__conuntOfFoodInManger != 0:
            foodForDelete = []
            for i in self.__volier:
                i: Animal
                if len(self.__manger) != 0:
                    for k in self.__manger:
                        if i._IsFedded == False:
                            i.eat(k)
                            if i._IsFedded == False:
                                if k in i._TypeOfFood:
                                    foodForDelete.append(k)
                                    self.__conuntOfFoodInManger -= 1
                    for j in foodForDelete:
                        self.__manger.remove(j)
                    foodForDelete.clear()
                elif len(self.__manger) == 0:
                    print('все съели')
                    return

    @property
    def foodInManger(self):
        if self.__conuntOfFoodInManger == 0:
            return 'тут пусто'
        else:
            print(self.__manger)
            return

    @property
    def needFoodAnimal(self):
        for i in self.__volier:
            i: Animal
            if i._EatenFood >= i._Food:
                i._IsFedded = True
                print(i.name + ':', i._IsFedded)
            else:
                print(i.name + ':', i._IsFedded, 'мне нужно что-то из этого:', i._TypeOfFood)
        return

    @property
    def doSound(self):
        for i in self.__volier:
            i: Animal
            i.voice
        return

    @property
    def sizeOfVolier(self):
        return self.__size

    @property
    def biomOfVolier(self):
        return self.__biom

    @property
    def nameOfVolier(self):
        return self.__name
