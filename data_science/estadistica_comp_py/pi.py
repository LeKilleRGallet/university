import random

def mean(X):
    return sum(X) / len(X)

def std(X):
    mean_x = mean(X)
    total = 0
    for x in X:
        total += (x - mean_x)**2
    return (total / len(X))**0.5

def throw_neddle(needles):
    needles_in = 0

    for _ in range (needles):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distance = (x**2 + y**2)**0.5

        if distance <= 1:
            needles_in += 1
        
    return (4 * needles_in) / needles

def estimation(needles,trys):

    results = []
    for _ in range(trys):
        results.append(throw_neddle(needles))

    print(f'with {needles} needles and {trys} trys, we get pi = {round(mean(results),5)} with a std of {round(std(results),5)}')
    return mean(results), std(results)
    
def pi_estimation(needles,trys, precision=0.01):

    while True:
        mean, std = estimation(needles, trys)
        
        if std < (precision/1.96):
            break
        else:
            needles *= 2

    return mean

def run():
    needles = int(input("How many needles do you want to throw? "))
    trys = int(input("How many trys do you want to do? "))
    pi_estimation(needles, trys)
    


if __name__ == "__main__":
    run()