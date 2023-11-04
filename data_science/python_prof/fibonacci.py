import time

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
    try:
        range_min = int(input('insert floor'))
    except ValueError:
        range_min = None

    try:
        range_max = int(input('insert ceil'))
    except ValueError:
        range_max = None
    
    if range_min is not None and range_max is not None and range_min >= range_max:
        raise SystemExit('Floor should be greater than or equal to ceil')


    fibonacci = FiboIter(min=range_min, max=range_max)
    for element in fibonacci:
        if element != None:
            print(element)
            time.sleep(0.05)

if __name__ == "__main__":
    run()