def remove_duplicates(some_list):
    """
    Remove duplicates from a list.
    """
    without_duplicates = []
    for item in some_list:
        if item not in without_duplicates:
            without_duplicates.append(item)
    return without_duplicates


def run():
    """
    docstring
    """
    some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(remove_duplicates(some_list))
    print(list(set(some_list))) ## remove duplicates using set()

if __name__ == "__main__":
    run()