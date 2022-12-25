from volier import *


class Zoo:
    def __init__(self, name: str, voliers: list):
        self.name = name
        self.__zoo = voliers
        self.__animalForRemove = []

    def removeAnimal(self, originVolier, reAnimal, newVolier):
        originVolier: Volier
        newVolier: Volier
        reAnimal: Animal
        for i in self.__zoo:
            i: Volier
            if i is originVolier:
                originVolier = i
        for i in self.__zoo:
            i: Volier
            if i is newVolier:
                newVolier = i
        if reAnimal not in originVolier._volier:
            return False
        elif originVolier.biomOfVolier != newVolier.biomOfVolier or newVolier.sizeOfVolier < reAnimal.size:
            return False
        else:
            newVolier.AddAnimal(reAnimal)
            originVolier.KillAnimal(reAnimal)
            return True

    def addAnimalInvolier(self, newAnimal, volier):
        if volier not in self.__zoo:
            return False
        elif volier in self.__zoo and type(newAnimal) != list:
            for i in self.__zoo:
                if volier is i:
                    volier = i
            volier: Volier
            volier.AddAnimal(newAnimal)
            return True
        elif volier in self.__zoo and type(newAnimal) == list:
            for i in self.__zoo:
                if volier is i:
                    volier = i
            volier: Volier
            for i in newAnimal:
                volier.AddAnimal(i)
            return True


    def addVolier(self, newVolier):
        if newVolier not in self.__zoo and type(newVolier) is Volier:
            self.__zoo.append(newVolier)
            return True
        elif newVolier in self.__zoo:
            return False
        else:
            return False


    def deleteVolier(self, delVolier):
        if delVolier not in self.__zoo:
            return False
        elif delVolier in self.__zoo:
            delVolier: Volier
            if delVolier._volier != []:
                return False
            elif delVolier._volier == []:
                return self.__zoo.remove(delVolier)

    @property
    def allVoliers(self):
        allVoliers = []
        for i in self.__zoo:
            i: Volier
            allVoliers.append(i.nameOfVolier)
        return allVoliers

    def allAnimalsInZoo(self):
        for i in self.__zoo:
            i: Volier
            print(i.nameOfVolier, ':', i.allAnimals)
        return

    def addFoodInvoliers(self, voliers: list, foodForZoo: list):
        if type(voliers) != list:
            return False
        if type(foodForZoo) != list:
            return False
        for i in voliers:
            if i not in self.__zoo:
                print('такого вольера нет:', i)
            elif i in self.__zoo:
                i: Volier
                i._addFoodInManger(foodForZoo)
        return True


    def foodInAllmangers(self):
        for i in self.__zoo:
            i: Volier
            print(i.nameOfVolier, ":", i.foodInManger)


    def neededFoodForAnimalsInVoliers(self):
        for i in self.__zoo:
            i: Volier
            if i._volier ==[]:
                print(i.nameOfVolier,':','здесь пока никто не живет')
            else:
                print(i.nameOfVolier, ":")
                i.needFoodAnimal
