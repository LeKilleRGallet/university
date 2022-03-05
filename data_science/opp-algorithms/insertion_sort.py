import random

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
            # print(f'list {i},{j}: {list}')

    return list


def run():

    list = [random.randint(0, 1000) for i in range(1000000)]
    print(f'generated list: {list}')
    
    print(f'insertion sorted list: {insertion_sort(list[:])}')

if __name__ == "__main__":
    run()