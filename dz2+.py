#Дополнительная домашка номер два нахрен
print('\n\nДоп задания!!!!!')
list = [5,1,89,2,3,4,0]
print(sorted(number*2 if number % 2 == 0 else number for number in list)) 


#ЧЕРЕЗ НАМПИ И РАНДОМ
import numpy as np
import random
try:
    k = int(input('Введи число строк матрицы: '))
    b = int(input('Введи число столбцов матрицы: '))
except ValueError:
    print('Это не число. Запусти заново и укажи число.')
matrix=np.random.randint(0,99,(k,b))
print(matrix)
#print((matrix[0]) что отображает первый элемент
sredvseh=[sum(sum(matrix[block]) for block in range(b))/(k*b)] #cреднее по всей больнице
sredkazhd=[sum(matrix[block])/k for block in range(b)] #среднее каждого элемента
print(sredvseh) 
print(sredkazhd)

#ВАРИАНТ ЧЕРЕЗ ЛИСТ
import random
try:
    k = int(input('Введи число строк матрицы: '))
    b = int(input('Введи число столбцов матрицы: '))
except ValueError:
    print('Это не число. Запусти заново и укажи число.')
matrix = [[random.randint(0,99) for i in range(k)] for d in range(b)]
print(matrix)
#делал для себя
#print(matrix[0])
#for blok in range(b): 
    #print(sum(matrix[blok]))
#sum(matrix[block]) for block in range(b) - cуммирует каждый блок столько раз, сколько указано, по очереди
sredvseh=[sum(sum(matrix[block]) for block in range(b))/(k*b)] #cреднее по всей больнице
sredkazhd=[sum(matrix[block])/k for block in range(b)] #среднее каждого элемента
print(sredvseh) 
print(sredkazhd)

#ПОСЛЕДНЕЕ ЗАДАНИЕ
matrix = [[random.randint(0,99) for i in range(3)] for d in range(3)]
tz=(matrix[0][0]+matrix[1][1]+matrix[2][2])
print(matrix)
print(tz)
