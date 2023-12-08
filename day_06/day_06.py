import pathlib
import re
from math import prod

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def calculate_number_of_ways_to_win(time, record):
    return len([x for x in range(1, time) if x * (time - x) > record])

if __name__ == "__main__":
    input = load_input()

    times = [int(x) for x in re.findall(r'[\d]+', input[0])]
    distance_records = [int(x) for x in re.findall(r'[\d]+', input[1])]

    print(prod(calculate_number_of_ways_to_win(times[i], distance_records[i]) for i in range(len(times))))

    time = int(input[0].replace(" ", "").replace("Time:", ""))
    distance_record = int(input[1].replace(" ", "").replace("Distance:", ""))
    print(calculate_number_of_ways_to_win(time, distance_record))