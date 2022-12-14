class Animal:

    def __init__(self, name, age=int, howmanyfoodeat=int, size=int, species=str,
                 habitat=str, typeOfFood=list, squad=str, voice=str, foodVoice=str):
        self._Name = name
        self._Food = howmanyfoodeat
        self.__Age = age
        self.__Size = size
        self.__Species = species
        self.__Habitat = habitat
        self._TypeOfFood = typeOfFood
        self.__Squad = squad
        self._Voice = voice
        self._FoodVoice = foodVoice
        self._IsFedded = False
        self._EatenFood = 0

    @property
    def needdedFood(self):
        return self._Food

    @property
    def isFedded(self):
        if self._EatenFood >= self._Food:
            self._IsFedded = True
            return self._IsFedded
        else:
            return self._IsFedded

    @property
    def name(self):
        return self._Name

    @name.setter
    def name(self, newName):
        if type(newName) == str:
            self._Name = newName
        else:
            print('tak nelzya')

    @property
    def squad(self):
        return self.__Squad

    @property
    def habitat(self):
        return self.__Habitat

    @property
    def species(self):
        return self.__Species

    @property
    def age(self):
        return self.__Age

    @age.setter
    def age(self, newAge):
        if newAge >= 0:
            self.__Age = newAge
        else:
            print("так нельзя")

    @property
    def size(self):
        return self.__Size

    @size.setter
    def size(self, newSize):
        if newSize >= 0:
            self.__Size = newSize
        else:
            print("так нельзя")


    def eat(self, food):
        if self._EatenFood < self._Food:
            if food in self._TypeOfFood:
                self._EatenFood += 1
                print(self._Name + ":", self._FoodVoice, '( потребил в пищу:', food, ')')
                return True
            elif food not in self._TypeOfFood:
                #я такое не ем#
                return 'я такое не ем'
        else:
            self._IsFedded = True
            print("я больше не буду")
            return 'я больше не буду'

    @property
    def voice(self):
        print(self._Name + ":", self._Voice)
        return

    @property
    def play(self):
        print(self._Name + ":", "*играет*")
        return

    @property
    def typeFood(self):
        return self._TypeOfFood