def fibonnacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnacci_recursive(n-1) + fibonnacci_recursive(n-2)

def dinamic_fibonacci(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = dinamic_fibonacci(n-1, memo) + dinamic_fibonacci(n-2, memo)
        memo[n] = result
        return result

def run():
    n = int(input("Enter a number: "))
    print(dinamic_fibonacci(n))

if __name__ == "__main__":
    run()