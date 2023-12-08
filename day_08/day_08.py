import pathlib
from math import lcm

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

class Instructions:
    def __init__(self, input):
        self.input = input
        self.length = len(input)

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        self.index += 1
        return self.input[self.index % self.length]

class Point:
    def __init__(self, input):
        parts = input.split(" = ")
        self.id = parts[0]
        destinations = parts[1].replace("(", "").replace(")", "").split(", ")
        self.left = destinations[0]
        self.right = destinations[1]
        
    def __getitem__(self, index):
        if index == "L":
            return self.left
        elif index == "R":
            return self.right
        else:
            print(index)
            return None

if __name__ == "__main__":
    input = load_input()
    
    map_points = dict([(p.id, p) for p in [Point(x) for x in input[2:]]])
    instructions = Instructions(input[0])

    current_position = map_points["AAA"]
    
    total_steps = 0
    directions = iter(instructions)
    while current_position.id != "ZZZ":
        total_steps += 1
        current_position = map_points[current_position[next(directions)]]

    print(total_steps)

    current_positions = [m for m in map_points.values() if m.id[2] == "A"]
    cycle_steps = []

    for position in current_positions:
        total_steps = 0
        directions = iter(instructions)
        current_position = position
        while current_position.id[2] != "Z":
            total_steps += 1
            current_position = map_points[current_position[next(directions)]]

        cycle_steps.append(total_steps)

    print(lcm(*cycle_steps))






