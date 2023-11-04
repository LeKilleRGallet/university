def run():
    palindrome = lambda string: string == string[::-1]

    print(palindrome('radar'))


if __name__ == "__main__":
    run()