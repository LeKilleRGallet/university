def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    """
    docstring
    """
    names = ["John", "Bob", "Mary", "Jane", "Matínez"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")

def run():
    """
    docstring
    """
    write()

if __name__ == "__main__":
    run()