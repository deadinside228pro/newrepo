class Whitebear:
    def __init__(self, name, howmanyfoodeat=float, age=int, size=float):
        self.__Name = name
        self.__Food = howmanyfoodeat
        self.__Age = age
        self.__Size = size
        self.__Species = "белый медведь"
        self.__Habitat = "Тундра"
        self.__TypeOfFood = ["рыба","ягоды","мясо"]
        self.__Squad = "всеядное"
        self.__Voice = "грааааарх"
        self.__IsFedded = False
        self.__EatenFood=0

    @property
    def needdedFood(self):
        return self.__Food


    @property
    def isFedded(self):
        if self.__EatenFood>=self.__Food:
            self.__IsFedded=True
            return print(self.__IsFedded)
        else:
            return print(self.__IsFedded)




    @property
    def name(self):
        return self.__Name
    @name.setter
    def name(self,newName):
        self.__Name=newName

    @property
    def age(self):
        return self.__Age
    @age.setter
    def age(self,newAge):
        if newAge>=0:
            self.__Age=newAge
        else:
            print("так нельзя")

    @property
    def size(self):
        return self.__Size
    @size.setter
    def size(self,newSize):
        if newSize>=0:
            self.__Size=newSize
        else:
            print("так нельзя")

    def eat(self, food):
        if self.__EatenFood < self.__Food:
            if food in self.__TypeOfFood:
                self.__EatenFood += 1
                return print(self.__Name + ":", "хрямкс *жуёт* хрумск ")
            if food not in self.__TypeOfFood:
                return print("я такое не ем")
        else:
            return print("я больше не буду")


    @property
    def voice(self):
        return print(self.__Name + ":",self.__Voice)




    @property
    def play(self):
        print(self.__Name + ":","*играет*")
