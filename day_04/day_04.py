import pathlib
import re

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

class Card:
    def __init__(self, line):
        parts = line.split(": ")
        self.card_number = int(parts[0].split(" ")[-1])
        numbers = parts[1].split(" | ")
        self.winning_numbers = set([int(x.group()) for x in re.finditer(r'[\d]+', numbers[0])])
        self.drawn_numbers = [int(x.group()) for x in re.finditer(r'[\d]+', numbers[1])]

    def calculate_score(self):
        number_of_matches = len([x for x in self.drawn_numbers if x in self.winning_numbers])
        return pow(2, number_of_matches - 1) if number_of_matches > 0 else 0
    
    def get_cards_won(self):
        number_of_matches = len([x for x in self.drawn_numbers if x in self.winning_numbers])
        return range(self.card_number + 1, self.card_number + number_of_matches + 1)

if __name__ == "__main__":
    input = load_input()

    cards = [Card(c) for c in input]

    print(sum([x.calculate_score() for x in cards]))

    counts = [1 for _ in cards]
    for card in cards:
        cards_won = card.get_cards_won()
        for winner in cards_won:
            counts[winner - 1] += counts[card.card_number - 1]

    print(sum(counts))

