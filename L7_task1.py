###################Лирическое отступление############################
#    я решил не использовать модуль Numpy для работы с матрицами,   #
# т.к. посчитал, что это было бы слишком просто и в задании указано,#
#         что необходимо разработать класс самостоятельно           #
#####################################################################


'''
Creating of class Matrix
-----------------------------------------------------------
Создание класса Matrix
'''
class Matrix:
    '''
    Overloading the class constructor - receiving data to form a matrix 
    ----------------------------------------------------------------------
    Перегрузка конструктора класса - приём данных для формирования матрицы
    '''
    def __init__(self, matrix):
        self.matrix = matrix
        
    '''
    Overloading the __str__ method - displaying the matrix in the usual form 
    (line by line, not as a list of lists) 
    ----------------------------------------------------------------------
    Перегрузка метода __str__ - вывод матрицы в привычном виде (построчно, 
    а не как список списков)
    '''
 
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix]) #возвращение матрицы в привычном виде
    
    '''
    Overloading the __add__ method for adding two matrices - elementwise 
    addition of matrix elements 
    -------------------------------------------------------------------------------------------
    Перегрузка метода __add__ для сложения двух матриц - поэлементное 
    сложение элементов матриц
    '''

    def __add__(self, another):
        if len(self.matrix) == len(another.matrix): #сравнение размеров двух складываемых матриц
            lenght = len(self.matrix[0]) #присвоение переменной lenght длины первого ряда матрицы
            for row in self.matrix: #перебор рядов первой матрицы
                if len(row) != lenght: #если длина очередного ряда не равна длине первого, вывод ошибки ValueError
                    raise ValueError(f"this row {row} is not equal to anothers in this matrix") 
            for row2 in another.matrix: #перебор рядов второй матрицы
                if len(row2) != lenght: #если длина очередного ряда не равна длине первого ряда первой матрицы, вывод ошибки ValueError
                    raise ValueError(f"this row {row} has not equal lenght to anothers matrix row")
            result = [] #создание промежуточных списков result и numbers
            numbers = []
            for i in range(len(self.matrix)): #поэлементный перебор и сложение элементов двух матриц (по рядам)
                for j in range(len(self.matrix[0])):
                    summ = another.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summ)
                    if len(numbers) == len(self.matrix[0]): #как только длина списка numbers равна длине первого ряда матриц
                        result.append(numbers) #добавление списка numbers к результату
                        numbers = [] #очистка промежуточного списка numbers
            return Matrix(result) #возвращение получившегося списка списков, приведённого к классу Matrix
        else: #вывод ошибки, если размеры складываемых матриц не одинаковы
            raise ValueError(f"Size of matrices\n{str(self.matrix)}\nand\n{str(another.matrix)}\nare not equal") 
        


'''
Creating two lists of lists to test how class Matrix works 
------------------------------------------------------------------------------
Создание двух списков из списков для проверки работы класса
'''
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

'''
Creation of two matrices from lists, displaying them on the screen, adding 
matrices, displaying the result 
------------------------------------------------------------------------------
Создание двух матриц из списков, вывод их на экран, сложение матриц, 
вывод на экран результата
'''
matrix1 = Matrix(list1)
matrix2 = Matrix(list2)
print(matrix1)
print("\n******************\n")
print(matrix2)
matrix3 = matrix1 + matrix2
print("\n******************\n")
print(matrix3)