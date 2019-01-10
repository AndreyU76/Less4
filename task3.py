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

python3.7 -m timeit -n 10 -s "import task2" "task2.Main()"

10 loops, best of 5: 154 nsec per loop - 10
100 loops, best of 5: 134 nsec per loop -100
1000 loops, best of 5: 131 nsec per loop -1000
