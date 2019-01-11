import cProfile
import functools

@functools.lru_cache()
def fi():
  
  return
b = [0]*8

for a in range(2,100):
    for c in range(2,10):
        if a%c == 0:
            b[c-2] += 1
a = 0
while a < len(b):
    print(a+2, ' - ', b[a])
    a += 1
    
if __name__ == "__main__":
    fi()
cProfile.run('fi()') 

2  -  49
3  -  33
4  -  24
5  -  19
6  -  16
7  -  14
8  -  12
9  -  11
         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
