import pathlib
import re

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    part_1_total = 0 
    height = len(input)
    width = len(input[0])

    grid = ['.' * (width + 2)]
    for line in input:
        grid.append('.' + line + '.')
    grid.append('.' * (width + 2))

    for y, line in enumerate(grid):
        numbers = re.finditer(r'[\d]+', line)
        for match in numbers:
            start_index = match.start() - 1
            end_index = match.end()

            if line[start_index] != '.':
                part_1_total += int(match.group())
                continue
            elif line[end_index] != '.':
                part_1_total += int(match.group())
                continue

            should_continue = False
            line_above = grid[y - 1]
            for i in range(start_index, end_index + 1):
                if not (line_above[i].isdigit() or line_above[i] == "."):
                    part_1_total += int(match.group())
                    should_continue = True
                    break
            if should_continue:
                continue

            should_continue = False
            line_below = grid[y + 1]
            for i in range(start_index, end_index + 1):
                if not (line_below[i].isdigit() or line_below[i] == "."):
                    part_1_total += int(match.group())
                    should_continue = True
                    break
            if should_continue:
                continue

    print(part_1_total)

    part_2_total = 0
    for y, line in enumerate(grid):
        potential_gears = re.finditer(r'\*', line)
        for gear in potential_gears:
            x = gear.start()
            test_string = grid[y - 1][x - 1:x + 2] + '.' + line[x - 1] + '.' + line[x + 1] + '.' + grid[y + 1][x - 1:x + 2]
            adjacent_numbers = re.findall(r'[\d]+', test_string)
            if (len(adjacent_numbers) == 2):
                # valid gear!
                numbers = [int(i.group()) for i in re.finditer(r'[\d]+', grid[y - 1]) if i.start() <= x + 1 and i.end() > x - 1] + \
                [int(i.group()) for i in re.finditer(r'[\d]+', line) if i.start() <= x + 1 and i.end() > x - 1] + \
                [int(i.group()) for i in re.finditer(r'[\d]+', grid[y + 1]) if i.start() <= x + 1 and i.end() > x - 1]
                if (len(numbers) != 2):
                    print('help', numbers)
                part_2_total += numbers[0] * numbers[1]


    print(part_2_total)