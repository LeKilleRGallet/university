def main():
    n = int(input())

    if primo(n):
        print("No Primo")
    else:
        print("Primo")

def primo(n):
    #validate if a number is prime
    if n<=1:
        return True
    elif n==2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return True
    



if __name__ == "__main__":
    main()