import random

def run():
    roll = int(input('how many dice? '))
    trys = int(input('how many times? '))

    roll_with_one = 0

    for _ in range(trys):
        rolls = []
        for _ in range(roll):
            rolls.append(random.randint(1,6))
        
        if 1 in rolls:
            roll_with_one += 1

    prob = roll_with_one/trys
    print(f'the probability of get at least one 1 in {roll} dice is {round(prob*100,2)}%')
    print(f'theorically it should be {round((1-(5/6)**roll)*100,2)}%')


if __name__ == "__main__":
    run()