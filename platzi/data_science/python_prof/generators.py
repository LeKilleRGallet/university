import time


def fibo_gen(r_min=None, r_max=None,):
    n1, n2 = 0,1
    while r_max == None or n1 <= r_max:
        if r_min == None or n1 >= r_min:
            yield n1
        n1, n2 = n2, n1 + n2



def run():
    try:
        range_min = int(input('insert floor'))
    except ValueError:
        range_min = None

    try:
        range_max = int(input('insert ceil'))
    except ValueError:
        range_max = None


    fibo = fibo_gen(range_min, range_max)
    for i in fibo:
        print(i)
        time.sleep(0.5)

if __name__ == "__main__":
    run()
