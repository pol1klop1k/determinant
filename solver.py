import math

def create(value, nums):        #функция, которая создает определитель
    nums = iter(nums)
    deter = [[] for k in range(value+1)]        #само тело определителя
    for k in range(1, value+1):
        deter[k].append('')       #создаю пустой элемент в каждой строке определителя для удобности индексов
        for n in range(value):
            deter[k].append(next(nums))     #добавляю в строку определителя элементы
    return deter

def minor(deter,i,j):           #функция, которая возвращает минор по строке i и столбцу j
    new = [[]]
    for k in range(1, len(deter)):
        new.append([''])
        for n in range(1, len(deter)):
            new[k].append(deter[k][n])
        new[k].pop(j)       #удаляем j элемент из каждой строки
    new.pop(i)              #удаляем i строку
    return new
