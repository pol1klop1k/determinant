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

def alg(deter, i, j):       #функция, которая вычисляет элемент со своим знаком i и j
    factor = deter[i][j]
    return factor * (-1)**(i+j)

def res(rem, cur=0):        #рекурсивная функция, которая считает определитель
    if len(rem) > 2:
        for i in range(1, len(rem)):
            cur += alg(rem, 1, i) * res(minor(rem, 1, i))       #заходим в рекурсию
        return cur
    else:
        cur = rem[1][1]     #возвращаем число, если остался определитель 1x1
        return cur
