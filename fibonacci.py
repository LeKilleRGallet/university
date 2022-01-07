import time

def prime(n):
    #validate if a number is prime
    if n<=1:
        return True
    elif n==2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            # print(i)
            if n%i==0:
                return True

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
    for element in fibonacci:
        if element != None:
            if fprime:
                if prime(element) != True:
                    print(f'{element: < {len(str(range_max))}} is a fibonacci prime [index: {fibonacci.counter}]')
            else:
                    print(element)
        time.sleep(0.05)

if __name__ == "__main__":
    run()