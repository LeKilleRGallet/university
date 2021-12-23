def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Enter a number: ")
    assert not(num.isalpha()), "You did not enter a number"
    assert int(num)>0, "Negative numbers are not valid"
    assert int(num)==0, "Zero have no divisors!"
    print(divisors(int(num)))

if __name__ == "__main__":
    run()

