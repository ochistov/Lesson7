from abc import ABC, abstractmethod

'''
Create a parent class AbstractClothes, create abstract methods 
--------------------------------------------------------------------------
Создание ролительского класса AbstractClothes, создание абстрактных методов
'''
class AbstractClothes(ABC):
    """ Интерфейс одежды """
    @property
    @abstractmethod
    def tissue_required(self): #требуемое на пошив количество ткани
        pass

    @property
    @abstractmethod
    def measuring(self): #размер одежды (общий)
        pass

    @abstractmethod
    def _calc_tissue_required(self): #расчёт требуемого кол-ва ткани
        pass

'''
Create a child class Clothes. Creating class methods.
----------------------------------------------------------------------------
Создание дочернего класса Clothes. Создание методов класса.
'''

class Clothes(AbstractClothes):
    _clothes = [] #полный список созданной одежды

    """ Одежда """
    def __init__(self, name, measuring):
        self.name = name #название одежды
        self._measuring = measuring #размер одежды
        self._tissue_required = None #необходимое кол-во ткани

        self._clothes.append(self) #добавление элемента одежды к списку одежды

    @property
    def tissue_required(self): #свойство - необходимое количество ткани для пошива
        if not self._tissue_required:
            self._calc_tissue_required()
        return self._tissue_required

    @property
    def measuring(self): #свойство - размер одежды
        return self._measuring

    @measuring.setter
    def measuring(self, measuring): #установка нового размера
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self): #свойство - количество ткани для пошива всей одежды
        return f"You total require {sum([item.tissue_required for item in self._clothes])} square meters of tissue"

'''
Create a Coat class as a child of the Clothes class. Overriding class methods 
------------------------------------------------------------------------------
Создание класса Coat, являющегося дочерним для класса Clothes. Переопределение 
методов класса
'''

class Coat(Clothes):
    def _calc_tissue_required(self): #расчёт расхода ткани на пальто
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self): #свойство - размер пальто
        return self.measuring

    @V.setter
    def V(self, size): #установка нового размера пальто
        self.measuring = size

    def __str__(self): #вывод на печать информации о названии пальто и кол-ве ткани для его пошива
        return f"To sew a {self.name} of size {self.measuring}, you will need {self.tissue_required} square meters of tissue"

'''
Create a Suit class as a child of the Clothes class. Overriding class methods 
-----------------------------------------------------------------------------
Создание класса Suit, являющегося дочерним для класса Clothes. Переопределение 
методов класса
'''
class Suit(Clothes):
    def _calc_tissue_required(self): #расчёт расхода ткани на пошив костюма
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self): #свойство - размер костюма
        return self.measuring

    @H.setter
    def H(self, height): #установка нового размера костюма
        self.measuring = height

    def __str__(self): #вывод на печать информации о названии костюма и кол-ве ткани для его пошива
        return f"To sew a {self.name} for growth {self.measuring}, you need {self.tissue_required} square meters of tissue"


'''
Checking the work of classes and methods, displaying the result on the screen 
-----------------------------------------------------------------------------
Проверка работы классов и методов, вывод результата на экран
'''
coat = Coat('Balenciaga coat', 5)
print(coat)
coat.V = 10
print(coat)

suit = Suit('Versace suit', 178)
print(suit)
suit.H = 200
print(suit)

print(coat.total_tissue_required)
print(suit.total_tissue_required)
