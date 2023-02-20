# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = (int (input('Введите количество элементов массива: ')))
res = random.sample(range(-10, 20), n)
maxi = (int (input('Введите максимальный элемент массива: ')))
mini = (int (input('Введите минимальный элемент массива: ')))
print(res)
if maxi > 20 and mini < -10:
    print ('Ошибка вода')

indices = [i for i in range(0, len(res)) if res[i] >= mini and res[i]<=maxi]
print(indices)
