def double_fac(num):
    double_fac = 1
    if num%2==0:
        start = 2
    else:
        start = 1
    for i in range(start,num+1,2):
        double_fac *= i
    return double_fac


num = int(input())

num = double_fac(num)

print(num)