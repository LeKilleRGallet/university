import random
from bokeh.plotting import figure, show


class Drunken:
    def __init__(self, name):
        self.name = name

class StandardDrunk(Drunken):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        return random.choice([(0,1), (0,-1), (1,0), (-1,0)])

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, delta_x, delta_y):
        return Coordinate(self.x + delta_x, self.y + delta_y)
    
    def dist(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y

        return (x_diff**2 + y_diff**2)**0.5

class Campus:
    def __init__(self):
        self.drunk_locations = {}

    def add_drunk(self, drunk, location):
        self.drunk_locations[drunk] = location

    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        current_location = self.drunk_locations[drunk]
        new_location = current_location.move(delta_x, delta_y)
        self.drunk_locations[drunk] = new_location

    def get_locations(self, drunk):
        return self.drunk_locations[drunk]

def graphwalk(x,y):
    graphic = figure(title='Random Walk', x_axis_label='Steps', y_axis_label='Distance')
    graphic.line(x, y)
    show(graphic)

def walk(step, drunk, campus):
    begin = campus.get_locations(drunk)

    # x_walk = [0]
    # y_walk = [0]

    for _ in range(step):
        campus.move_drunk(drunk)

        ##### graph the walk #####
    #     current_location = campus.get_locations(drunk)
    #     x_walk.append(current_location.x)
    #     y_walk.append(current_location.y)
    
    # graphwalk(x_walk, y_walk)

    ##################################################


    return begin.dist(campus.get_locations(drunk))

def simulate(step, trys, drunk_type):
    drunk = drunk_type(name='Joe Doe')
    origin = Coordinate(0, 0)
    distances =[]

    for _ in range(trys):
        campus = Campus()
        campus.add_drunk(drunk, origin)
        simulation = walk(step, drunk, campus)

        distances.append(simulation)

    return distances

def graph(x, y):
    graphic = figure(title='Random Walk', x_axis_label='Steps', y_axis_label='Distance')
    graphic.line(x, y)
    show(graphic)

def main(distance, trys, drunk_type):
    means = []
    for step in distance:
        distances = simulate(step, trys, drunk_type)

        mean_dist = round( sum(distances) / len(distances), 2)
        max_dist = round( max(distances), 2)
        min_dist = round( min(distances), 2)

        print(f'{drunk_type.__name__} walked {step} steps')
        print(f'Mean: {mean_dist}')
        print(f'Max: {max_dist}')
        print(f'Min: {min_dist}')
        print()
    
        means.append(mean_dist)
    
    graph(distance, means)


def run():
    


    distance = [*range(0, 10000, 100)]
    trys = 100

    main(distance, trys, StandardDrunk)



if __name__ == "__main__":
    run()