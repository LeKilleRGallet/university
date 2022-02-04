def printabundant(abundant):
    for i in abundant:
        print(i)

def isabundant(floor, ceil, abundant):
    for i in range(floor,ceil+1):
        sum=0
        for j in range(1,i+1):
            if i%j==0:
                sum+=j
        if sum>(2*i):
            abundant.append(i)

def getnumber():
    num = int(input())
    return num

def run():
    floor= getnumber()
    ceil= getnumber()
    abundant=[]
    isabundant(floor,ceil,abundant)
    printabundant(abundant)


if __name__ == "__main__":
    run()