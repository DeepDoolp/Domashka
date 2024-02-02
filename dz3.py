#Основное:
#1. Есть x = [1,2,3,4,5], сгенерировать новый list, в котором каждый элемент умножается на 2
#2. Есть произвольный list, сгенерировать новый list, в котором возводится в квадрат каждый четный элемент, а каждый нечетный заменяется на 0
#3. Написать функцию, которая принимает строку, убирает все пробелы со строки и возвращает ее
#4. Написать функцию, которая работает только с list, и возвращает reversed list
#5. Написать функцию, которая принимает только list, возвращает кол-во нулей в list


# задание 1
x = [1,2,3,4,5]
print([pop*2 for pop in x])

# задание 2
import random
proizvol = [random.randint(0,99) for i in range(7)]
print(proizvol)
print([item**2 if item%2==0 else 0 for item in proizvol])

# задание 3, решить потом другим способом
def hateprob(a):
        print("Ненавижу блять пробелы! Вот так надо: ")
        stroka=''.join(["" if bukva == " " else bukva for bukva in a])
        print(stroka)
        return(stroka)
hateprob((input("Введи че хочешь: ")))

#задание 4 
def listonly(a):
        if isinstance(a, list) == True:
                b=list(reversed(a))
                return(b)
        else:
                print('Это не лист, введи лист')
                
print(listonly(100))
print(listonly('kwlww'))
print(listonly([1,2,125]))

#задание 5
def listcount(a):
        if isinstance(a, list) == True:
                b=0
                for item in a:
                        if item == 0:
                                b+=1
                        else:
                                pass
                return(b)
        else:
                print('Это не лист, введи лист')
print(listcount([1,5,16,0,24,0,0,0,0,00,0,0,5]))

                