from animal import Animal


class volier:
    def __init__(self,name,biom,size,squad):
        self.__volier=[]
        self.__name=name
        self.__biom=biom
        self.__size=size
        self.__squad=squad



    def AddAnimal(self,newanimal: Animal):
        if self.__biom == newanimal.habitat and self.__size>newanimal.size and self.__squad == newanimal.squad :
            self.__volier.append(newanimal)
        elif self.__biom !=newanimal.habitat and :
            print('я тут жить не смогу')
        
        
