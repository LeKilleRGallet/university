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

def estimation(needles,tries):

    results = []
    for _ in range(tries):
        results.append(throw_neddle(needles))

    print(f'with {needles} needles and {tries} tries, we get pi = {round(mean(results),5)} with a std of {round(std(results),5)}')
    return mean(results), std(results)
    
def pi_estimation(needles,tries, precision=0.01):

    while True:
        mean, std = estimation(needles, tries)
        
        if std < (precision/1.96):
            break
        else:
            needles *= 2

    return mean

def run():
    needles = int(input("How many needles do you want to throw? "))
    tries = int(input("How many tries do you want to do? "))
    pi_estimation(needles, tries)
    


if __name__ == "__main__":
    run()