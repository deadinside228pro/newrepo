from volier import *

class Zoo:
    def __init__(self, name, voliers=list):
        self.name = name
        self.__zoo = voliers
        self.__animalForRemove = []

    def removeAnimal(self, originVolier, reAnimal, newVolier):
        originVolier: Volier
        newVolier: Volier
        reAnimal: Animal
        for i in self.__zoo:
            i:Volier
            if i is originVolier:
                originVolier = i
        for i in self.__zoo:
            i: Volier
            if i is newVolier:
                newVolier = i
        if reAnimal not in originVolier.allAnimals:
            return False
        elif originVolier.biomOfVolier != newVolier.biomOfVolier or newVolier.sizeOfVolier < reAnimal.size:
            return False
        else:
            return newVolier.AddAnimal(reAnimal)







    @property
    def allVoliers(self):
        allVoliers = []
        for i in self.__zoo:
            i: Volier
            allVoliers.append(i.nameOfVolier)
        return allVoliers




