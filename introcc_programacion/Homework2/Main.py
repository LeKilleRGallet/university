x_1 =float(input())
y_1 =float(input())
r_1 =float(input())
x_2 =float(input())
y_2 =float(input())
r_2 =float(input())

d = ((x_2-x_1)**2+(y_2-y_1)**2)**(1/2)

if (d <= abs(r_1+r_2) and d > abs(r_2-r_1))  or d == abs(r_2-r_1):
    print('true') 
else:
    print('false')