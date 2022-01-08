import time
from datetime import datetime
import os

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def prime_validator(n, primes):
    if n<=1:
        return True
    elif n in (2,3,5,7):
        return False
    else:
        sqrt_n = n**0.5
        if n == int(sqrt_n)**2:
            return True
        else:
            for i in primes:
                if i > (int(sqrt_n)+1):
                    return False
                if n%i == 0:
                    return True

def prime(element, primes):
    while True:
        try:
            if element not in (2,3,5,7) and 0 in {element%2, element%3, element%5, element%7}:
                return True
            else:
                if primes[-1]>(element**0.5):
                    if prime_validator(element, primes) != True:
                        return False
                    else:
                        return True
                else:
                    for i in range(primes[-1]+1, round(element**0.5)+2):
                        if prime_validator(i, primes) != True:
                            primes.append(i)
                    if primes[-1]<(element**0.5):
                        for i in range(primes[-1]+1, primes[-1]**2):
                            if prime_validator(i, primes) != True:
                                primes.append(i)
                                break
        except IndexError:
            if element <= 1:
                return True
            elif element == 2:
                primes.append(element)
                return False

class FiboIter():

    def __init__(self,min=None, max=None):
        self.min = min
        self.max = max


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        
        if self.counter == 0:
            if self.max is None or self.n1 <= self.max:
                self.counter += 1
                if self.min is None or self.n1 >= self.min:
                    return self.n1
            else:
                raise StopIteration
        elif self.counter == 1:
            if self.max is None or self.n2 <= self.max:
                self.counter += 1
                if self.min is None or self.n2 >= self.min:
                    return self.n2
            else:
                raise StopIteration
        else:
            self.aux = self.n1 + self.n2
            if self.max is None or self.aux <= self.max:
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                if self.min is None or self.aux >= self.min:
                    return self.aux
            else:
                raise StopIteration

def run():
    clear()
    primes=[]
    while True:
        try:
            range_min = input('insert floor: ')
            if range_min == '':
                range_min = None
                break
            else:
                range_min = int(range_min)
                break
        except ValueError:
            print("Invalid input, just integers or empty, please try again")

    while True:
        try:
            range_max = input('insert ceil: ')
            if range_max == '':
                range_max = None
                break
            else:
                range_max = int(range_max)
                break
        except ValueError:
            print("Invalid input, just integers or empty, please try again")
    
    if range_min is not None and range_max is not None and range_min >= range_max:
        raise SystemExit('Floor should be greater than or equal to ceil')
    
    fprime = input('do u wanna see only prime numbers? (y/n): ')
    while True:
        if fprime == 'y':
            fprime = True
            break
        elif fprime == 'n':
            fprime = False
            break
        else:
            fprime = input('Invalid input, just y or n, please try again: ')

    fibonacci = FiboIter(min=range_min, max=range_max)

    c = 1
    lrange_max = 0

    if fprime and range_min != None:
        for i in range((range_min**0.5)+1):
            if prime_validator(i, primes) != True:
                primes.append(i)

    if fprime and range_max != None:
        lrange_max = len(str(range_max))
    elif fprime and range_max == None:
        lrange_max = 17

    time_0 = datetime.now()
    for element in fibonacci:
        if element != None:
            if fprime:
                if prime(element, primes) != True:
                    print(f'{str(c)+")":>3}{element: > {lrange_max}} is a fibonacci prime [index: {fibonacci.counter:>3}] Execution time: {str((datetime.now() - time_0).total_seconds()):>8} seconds')
                    c += 1
                    time_0 = datetime.now()
            else:
                    print(element)
        time.sleep(0.05)

if __name__ == "__main__":
    run()