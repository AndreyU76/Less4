# Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
# то во второй массив надо заполнить значениями 1, 4, 5, 6 
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
# -*- encoding: utf-8 -*-

def Main():
    return(N)

from random import random
N = 100000000
arr = [0]*N
even = []
for a in range(N):
    arr[a] = int(random() * 10) + 10
    if arr[a] % 2 == 0:
        even.append(a)
#print(arr)
#print('Индексы четных элементов: ', even)

if __name__ == "__main__":
    Main()

10 loops, best of 5: 154 nsec per loop - 10
100 loops, best of 5: 134 nsec per loop -100
1000 loops, best of 5: 131 nsec per loop -1000
