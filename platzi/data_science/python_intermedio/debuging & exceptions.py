def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Enter a number: "))
        try:
            if num == 0:
                raise ValueError("Zero have no divisors!")
            elif num<0:
                raise ValueError("Negative numbers are not valid.")
            else:
                print(divisors(num))
                print("end")
        except ValueError as err:
            print("Error:", err)
            print("end")
    except ValueError:
        print("You did not enter a number")

if __name__ == "__main__":
    run()