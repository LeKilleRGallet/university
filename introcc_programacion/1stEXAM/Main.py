n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

if n_1 == n_2 == n_3:
    n_1a = 1
    n_2a = 2
    n_3a = 3
elif n_1 == n_2 or n_1 == n_3 or n_2 == n_3:
    if n_1 == n_2 > n_3:
        n_1a = 2
        n_2a = 3
        n_3a = 1
    elif n_1 == n_3 > n_2:
        n_1a = 2
        n_2a = 1
        n_3a = 3
    elif n_2 == n_3 > n_1:
        n_1a = 1
        n_2a = 2
        n_3a = 3
    elif n_1 == n_2 < n_3:
        n_1a = 1
        n_2a = 2
        n_3a = 3
    elif n_1 == n_3 < n_2:
        n_1a = 1
        n_2a = 3
        n_3a = 2
    elif n_2 == n_3 < n_1:
        n_1a = 3
        n_2a = 1
        n_3a = 2
elif n_1 > n_2 > n_3:
    n_1a = 3
    n_2a = 2
    n_3a = 1
elif n_1 > n_3 > n_2:
    n_1a = 3
    n_2a = 1
    n_3a = 2
elif n_2 > n_3 > n_1:
    n_1a = 1
    n_2a = 3
    n_3a = 2
elif n_2 > n_1 > n_3:
    n_1a = 2
    n_2a = 3
    n_3a = 1
elif n_3 > n_1 > n_2:
    n_1a = 2
    n_2a = 1
    n_3a = 3
elif n_3 > n_2 > n_1:
    n_1a = 1
    n_2a = 2
    n_3a = 3

print("%d\n%d\n%d" % (n_1a, n_2a, n_3a))