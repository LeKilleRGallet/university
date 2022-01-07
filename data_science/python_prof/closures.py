def make_division(n):
    def division_by(x):
        assert n != 0, "n must not be zero"
        return x / n
    return division_by

def run():
    division_5 = make_division(5)
    division_10 = make_division(10)
    print(division_5(100))
    print(division_10(100))

if __name__ == "__main__":
    run()