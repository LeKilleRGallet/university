# validate the input if a multiple of 5 if is true then return the five table 

n = int(input())

if n % 5 == 0:
    i = 5
    while i <= n:
        print(i)
        i += 5

else:
    print("error")