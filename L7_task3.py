'''
Creating the Cell class, overriding the methods addition (__add __ ()), 
subtraction (__sub __ ()), multiplication (__mul __ ()), division (__truediv __ ()) 
-----------------------------------------------------------------------------
Создание класса Cell, переопределение методов сложение (__add__()), 
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__())
'''
class Cell:
    def __init__(self, count):
        self._count = count

    def __add__(self, other): #переопределение метода "сложение"
        return Cell(self._count + other._count)

    def __sub__(self, other): #переопределение метода "вычитание" 
        if self._count > other._count:
            return Cell(self._count - other._count)

       # raise ValueError(f"{self._count} - {other._count}: impossible operation") - нормальный выход при ошибке с отрицательным результатом при вычитании
        print(f"{self._count} - {other._count}: impossible operation") #костыль вывода ошибки, чтобы не ломать программу и дать ей отработать до конца :)

    def __mul__(self, other): #переопределение метода "умножение"
        return Cell(self._count * other._count)

    def __truediv__(self, other): #переопределение метода "деление"
        return Cell(self._count // other._count)

    def make_order(self, per_row): #реализация метода организации ячеек по рядам
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self): #переопределение метода str для вывода количества ячеек в клетке
        return f"Клетка состоит из {self._count} ячеек"


'''
Testing the class and methods 
------------------------------------------------------------------
Проверка работы класса и методов
'''
c1 = Cell(15)
print(c1)
c2 = Cell(13)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c2 - c2)
print(c1 * c2)
print(c1 / c2)
print((c1).make_order(5))
