from animal import *


class Volier:
    def __init__(self, name, biom, size):
        self._volier = []
        self.__name = name
        self.__biom = biom
        self.__size = size
        self._manger = []
        self.__conuntOfFoodInManger = 0

    @property
    def allAnimals(self):
        animalsInVolier = []
        for i in self._volier:
            i: Animal
            animalsInVolier.append(i.name)
        return animalsInVolier



    def AddAnimal(self, animal_new: Animal):
        if len(self._volier) == 0 and self.__biom == animal_new.habitat and self.__size >= animal_new.size:
            self.__size -= animal_new.size
            self._volier.append(animal_new)
            return True
        if animal_new in self._volier:
            return "there is can not be two similar animals"
        if self.__biom != animal_new.habitat:
            return 'он здесь не уживётся'
        if self.__size < animal_new.size:
            return False
        if self.__biom == animal_new.habitat and self.__size >= animal_new.size:
            for i in self._volier:
                i: Animal
                if i.squad == 'хищное' and i.species == animal_new.species:
                    self.__size -= animal_new.size
                    self._volier.append(animal_new)
                    return True
                elif i.squad == 'травоядное':
                    self.__size -= animal_new.size
                    self._volier.append(animal_new)
                    return True
        else:
            print('он здесь не уживётся')
            return

    def KillAnimal(self, animal):
        if animal in self._volier:
            animal: Animal
            self.__size += animal.size
            return self._volier.remove(animal)
        else:
            return False

    def EatFood(self, food1: list):
        if type(food1) != list:
            print('передай, пожалуйста, лист с едой')
            return False
        for k in food1:
            self._manger.append(k)
            self.__conuntOfFoodInManger += 1
        if self.__conuntOfFoodInManger == 0:
            print('кормушка пуста')
            return 'кормушка пуста'
        elif self.__conuntOfFoodInManger != 0:
            foodForDelete = []
            for i in self._volier:
                i: Animal
                if len(self._manger) != 0:
                    for k in self._manger:
                        if i._IsFedded == False:
                            i.eat(k)
                            if i._IsFedded == False:
                                if k in i._TypeOfFood:
                                    foodForDelete.append(k)
                                    self.__conuntOfFoodInManger -= 1
                    for j in foodForDelete:
                        self._manger.remove(j)
                    foodForDelete.clear()
                elif len(self._manger) == 0:
                    print('все съели')
                    return 'все съели'

    @property
    def foodInManger(self):
        if self.__conuntOfFoodInManger == 0:
            return 'тут пусто'
        else:
            return self._manger


    @property
    def needFoodAnimal(self):
        for i in self._volier:
            i: Animal
            if i._EatenFood >= i._Food:
                i._IsFedded = True
                print(i.name + ':', i._IsFedded)
                return True
            else:
                print(i.name + ':', i._IsFedded, 'мне нужно что-то из этого:', i._TypeOfFood)
        return False

    @property
    def doSound(self):
        for i in self._volier:
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

    def _addFoodInManger(self, food: list):
        if type(food) != list:
            return False
        else:
            for i in food:
                self._manger.append(i)
                self.__conuntOfFoodInManger += 1
            return self._manger


