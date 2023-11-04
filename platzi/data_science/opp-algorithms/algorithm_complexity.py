import time
from math import factorial
import matplotlib.pyplot as plt
from sys import setrecursionlimit


setrecursionlimit(1000000)

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def non_recursive_factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        i=1
        while i <= n:
            result *= i
            i += 1
        return result

def algorith_complexity_graph(recursive_list, non_recursive_list, n):
    x=[*range(n+1)]
    plt.plot(x, recursive_list, label='Recursive')
    plt.plot(x, non_recursive_list, label='Non-Recursive')
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.title('Algorithm Complexity')
    plt.legend()
    plt.show()





def run():
    n = int(input('n: '))
    recursive_time=[]
    non_recursive_time=[]
    i=0
    recursive_factorial(n)
    non_recursive_factorial(n)
    while i <= n:
        print(f'\t\t{i} / {n}', end='\r')
        start = time.time()
        recursive_factorial(i)
        end = time.time()
        recursive_time.append(end-start)
        start = time.time()
        non_recursive_factorial(i)
        end = time.time()
        non_recursive_time.append(end-start)
        i += 1

    algorith_complexity_graph(recursive_time, non_recursive_time, n)
    




if __name__ == "__main__":
    run()