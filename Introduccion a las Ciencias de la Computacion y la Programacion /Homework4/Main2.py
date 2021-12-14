#Strong prime validator

def main():
    n = int(input())

    if primo(n):
        print("No es Primo Fuerte")
    elif n ==2:
        print("No es Primo Fuerte")
    else:
        #In number theory, a strong prime is a prime number that is greater than the arithmetic mean of the nearest prime above and below  
        if n>(primosig(n)+primoant(n))/2:
            print("Primo Fuerte")
        else:
            print("No es Primo Fuerte")
        

def primo(number):
    #validate if a number is prime
    if number<=1:
        return True
    elif number==2:
        return False
    else:
        for i in range(2,int(number**(1/2))+1):
            if number%i==0:
                return True

def primosig(n):
    #search the nearest prime number below n
    for i in range(n+1,n+100):
        if primo(i)!=True:
            return i

def primoant(n):
    #search the nearest prime number above n
    for i in range(n-1,1,-1):
        if primo(i)!=True:
            return i




if __name__ == "__main__":
    main()