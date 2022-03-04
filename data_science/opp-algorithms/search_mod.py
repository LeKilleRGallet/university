import random
import time
import matplotlib.pyplot as plt

def sequential_search(list, item):
    #O(n)
    trys=0
    for element in list:
        trys += 1
        if element == item:
            break
            
    return trys

def binary_search(list, item):
    #O(log n)
    low=0
    high=len(list)-1

    trys=0

    while low <= high:
        trys += 1

        mid=(low+high)//2
        guess=list[mid]
        if guess == item:
            break
        if guess > item:
            high=mid-1
        else:
            low=mid+1

    return trys

def scatter_trys(n,trys):
    plt.scatter(n,trys)
    plt.xlabel('n')
    plt.ylabel('difference in tries (seq-bin)')
    plt.title('Scatter plot of difference in tries (seq-bin)')
    plt.show()

def run():
    diff_trys=[]
    n=[]
    last=100
    mx=random.randint(1,last)
    for _ in range(mx):
        print(f'\t\t{_+1} / {mx}', end='\r')

        list_size=random.randint(1,last)
        n.append(list_size)
        item=random.randint(0,list_size*2)

        list=sorted([random.randint(0,list_size*2) for _ in range(list_size)])

        bin_try=binary_search(list, item)
        seq_try=sequential_search(list, item)
        print(f"'bin: '{bin_try}', seq: '{seq_try}", end = '\t')
        diff_trys.append(seq_try-bin_try)
        print(f'diff: {seq_try-bin_try}')

    print(f'total diff is: {sum(diff_trys)}')
    scatter_trys(n,diff_trys)




if __name__ == "__main__":
    run()