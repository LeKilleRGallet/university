import random

def merge(left, right):
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list += left[i:]
    merged_list += right[j:]
    return merged_list

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def run():
    
    list = [random.randint(0, 10000) for i in range(1000000)]
    print(f'generated list: {list}')
    print(f'merge sorted list: {merge_sort(list[:])}')

if __name__ == "__main__":
    run()