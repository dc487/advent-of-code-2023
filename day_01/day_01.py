import pathlib
import re

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    digits = [re.sub(r'[^\d]', '', x) for x in input]

    print(sum([int(x[0] + x[-1]) for x in digits if len(x) > 1]) + sum([int(x[0] + x[0]) for x in digits if len(x) == 1]))

    replacements = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    digits2 = [replacements[re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', x)[0]] + replacements[re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', x[::-1])[0][::-1]] for x in input]

    print(sum([int(x) for x in digits2]))
    