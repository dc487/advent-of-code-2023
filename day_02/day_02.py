import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

class Draw:
    def __init__(self, input):
        self.results = {"blue": 0, "red": 0, "green": 0}
        for x in input.split(", "):
            y = x.split(" ")
            self.results[y[1]] += int(y[0])

    def draw_possible(self):
        return self.results["red"] <= 12 and self.results["green"] <= 13 and self.results["blue"] <= 14

class Game:
    def __init__(self, input):
        game = input.split(": ")
        self.id = int(game[0].split(" ")[1])
        self.draws = [Draw(x) for x in game[1].split("; ")]

    def calculate_power(self):
        return max([d.results["red"] for d in self.draws]) * max([d.results["green"] for d in self.draws]) * max([d.results["blue"] for d in self.draws])

if __name__ == "__main__":
    input = load_input()

    games = [Game(x) for x in input]

    print(sum([g.id for g in games if all([d.draw_possible() for d in g.draws])]))
    print(sum([g.calculate_power() for g in games]))
