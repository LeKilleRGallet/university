### last name, first name to first name last name

def save_file(filename, names):
    with open(filename, 'w') as f:
        for name in names:
            f.write(name + '\n')

def read_file(filename):
    names=[]
    with open(filename, 'r') as f:
        for line in f:
            name = line.split(',')
            names.append(name[1].strip() + ' ' + name[0].strip())
    return names
def run():

    file=input('write the name of the file: ')

    names=read_file(file)
    save_file(file, names)

if __name__ == "__main__":
    run()