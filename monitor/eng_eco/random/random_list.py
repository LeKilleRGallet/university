import random

def read_file(filename):
    names=[]
    with open(filename, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names

def run():
    file=input('write the name of the file: ')
    names=read_file(file)

    for _ in range(random.randint(1,10)):
        random.shuffle(names)

    for i in range(len(names)):
        print(f'{i+1}. {names[i]}')

if __name__ == "__main__":
    run()