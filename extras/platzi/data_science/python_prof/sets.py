set1 = {1,2,3,4,5,6,7,8,9}
set2 = {5,6,7,8,9,10,11,12,13}

union_set = set1 | set2 # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} // set1.union(set2)
intersection_set = set1 & set2 # {5, 6, 7, 8, 9} // set1.intersection(set2)
difference_set = set1 - set2 # {1, 2, 3, 4} // set1.difference(set2)
symmetric_difference_set = set1 ^ set2 # {1, 2, 3, 4, 10, 11, 12, 13} // set1.symmetric_difference(set2)

print(f"set1: {set1} and set2: {set2} union set is: {union_set}")
print(f"set1: {set1} and set2: {set2} intersection set is: {intersection_set}")
print(f"set1: {set1} and set2: {set2} difference set is: {difference_set}")
print(f"set1: {set1} and set2: {set2} symmetric difference set is: {symmetric_difference_set}")
