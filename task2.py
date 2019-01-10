import cProfile

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
cProfile.run('Main()') 
4 function calls in 0.015 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 22.py:3(Main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.015    0.015    0.015    0.015 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


