print('I задание')
a = -5
while a <= 5:
    print(a)
    a += 1

print('II задание')
summ = 0
a = int(input('задайте начало диапазона: '))
b = int(input('задайте конец диапазона: '))
if a > b:
    while b <= a:
        summ += summ + b
        b = b + 1
    print(summ)
elif a < b:
    while a <= b:
        summ = summ + a
        a = a + 1
    print(summ)
else:
    print('это нихуя не диапазон, это одинаковое число, дебил')

print('III задание')
summ = 0
a = int(input('задайте начало диапазона: '))
b = int(input('задайте конец диапазона: '))
c = 0
if a > b:
    while b <= a:
        summ += summ + b
        b = b + 1
        c += 1
    print('среднее арифмитическое:', summ / c)
elif a < b:
    while a <= b:
        summ = summ + a
        a = a + 1
        c += 1
    print('среднее арифмитическое:', summ / c)
else:
    print('это нихуя не диапазон, это одинаковое число, дебил')

print('IV задание')
a = int(input('задайте начало диапазона: '))
b = int(input('задайте конец диапазона: '))
c=0
if a > b:
    while b <= a:
        if b < 0:
            c += 1
        b = b + 1
    print (c)
elif a < b:
    while a <= b:
        if a < 0:
            c += 1
        a=a+1
    print(c)
else:
    print('это нихуя не диапазон, это одинаковое число, дебил')


print('V задание')
a = int(input('задайте начало диапазона: '))
b = int(input('задайте конец диапазона: '))
c=1
if a<b:
    for i in range (a,b+1):
        if i < 0 and i%2==0:
            c*=i
    print("Результат умножения нечетных отрицательных чисел:", c)
else:
    print('первое число должно быть меньше второго')
    
