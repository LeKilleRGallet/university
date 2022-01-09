from datetime import datetime
import os

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def fiboiter(r_min=None, r_max=None):
    n1, n2 = 0,1
    while r_max == None or n1 <= r_max:
        if r_min == None or n1 >= r_min:
            yield n1
        n1, n2 = n2, n1 + n2

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
            elif element > 2:
                primes.append(2)

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

    fibonacci = fiboiter(r_min=range_min, r_max=range_max)

    index = 1
    counter = 1
    lrange_max = 0
    
    if range_min is not None:
        for i in fiboiter(r_max=range_min-1):
            index += 1
    

    if fprime and range_max != None:
        lrange_max = len(str(range_max))
    elif fprime and range_max == None:
        lrange_max = 17

    time_0 = datetime.now()
    for element in fibonacci:
        if element != None:
            if fprime:
                if prime(element, primes) != True:
                    print(f'{str(counter)+")":>3}{element: > {lrange_max}} is a fibonacci prime [index: {index:>3}] Execution time: {str((datetime.now() - time_0).total_seconds()):>8} seconds')
                    counter += 1
                    time_0 = datetime.now()
            else:
                    print(element)
        index += 1
        # time.sleep(0.05)

if __name__ == "__main__":
    run()