def run():
    # cube = {}

    # for i in range(1, 101):
    #     if i%3!=0:
    #         cube[i] = i ** 3
    # print(cube)

    cube = {i:i**3 for i in range(1,101) if i % 3 != 0}
    # print(cube)

    root = {i:round(i**0.5,2) for i in range(1,1001)}
    print(root)

if __name__ == "__main__":
    run()
