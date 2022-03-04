import random
import time

def sequential_search(list, item):
    #O(n)
    for element in list:
        if element == item:
            return True
            
    return False

def binary_search(list, item):
    #O(log n)
    low=0
    high=len(list)-1

    trys=0

    while low <= high:
        trys += 1
        # print(f'searching between {list[low]} and {list[high]}')
        # time.sleep(1)

        mid=(low+high)//2
        guess=list[mid]
        # print(f'guess is {guess}')
        if guess == item:
            print(f'trys: {trys}')
            return True
        if guess > item:
            # print(f'{guess} is greater than {item}')
            high=mid-1
        else:
            # print(f'{guess} is less than {item}')
            low=mid+1
        
        
    print(f'trys: {trys}')
    return False

def run():
    list_size=int(input('Enter the size of the list: '))
    item=int(input('Enter the item to search: '))
    while item < 0 or item > list_size*list_size:
        item=int(input('Enter the item to search: '))

    list=sorted([random.randint(0,list_size*2) for i in range(list_size)])

    print(f'The list is: {list}')
    # print(f'The item {item} {("is" if sequential_search(list, item) else "is not")} in the list')
    print(f'The item {item} {("is" if binary_search(list, item) else "is not")} in the list')



if __name__ == "__main__":
    run()