import pathlib
from collections import Counter

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

class Hand:
    def __init__(self, line):
        parts = line.split(" ")

        card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

        self.bid = int(parts[1])
        self._original = parts[0]
        self.cards = [card_values[c] for c in parts[0]]

        counts = Counter(self.cards)

        if any([c for c in counts.values() if c == 5]): # five of a kind
            self.type = 6
        elif any([c for c in counts.values() if c == 4]): # four of a kind
            self.type = 5
        elif any([c for c in counts.values() if c == 3]):
            if any([c for c in counts.values() if c == 2]): # full house
                self.type = 4
            else: # 3 of a kind
                self.type = 3 
        elif len([c for c in counts.values() if c == 2]) == 2: # two pair
            self.type = 2
        elif any([c for c in counts.values() if c == 2]): # one pair
            self.type = 1
        else: # High Card
            self.type = 0
 
        self.sort_value = self.type * pow(10,10) + self.cards[0] * pow(10,8) + self.cards[1] * pow(10,6) + self.cards[2] * pow(10,4) + self.cards[3] * 100 + self.cards[4]

class Hand2:
    def __init__(self, line):
        parts = line.split(" ")

        card_values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

        self.bid = int(parts[1])
        self._original = parts[0]
        self.cards = [card_values[c] for c in parts[0]]

        counts = Counter([c for c in self.cards if c != 1])
        total_jokers = Counter(self.cards)[1]

        if any([c for c in counts.values() if c + total_jokers == 5]) or total_jokers == 5: # five of a kind
            self.type = 6
        elif any([c for c in counts.values() if c + total_jokers == 4]): # four of a kind
            self.type = 5
        elif any([c for c in counts.values() if c + total_jokers == 3]):
            if total_jokers == 0:
                if any([c for c in counts.values() if c == 2]): # full house
                    self.type = 4
                else: # 3 of a kind
                    self.type = 3 
            else:
                if len([c for c in counts.values() if c == 2]) > 1: # full house
                    self.type = 4
                else: # 3 of a kind
                    self.type = 3
        elif len([c for c in counts.values() if c == 2]) == 2: # two pair
            self.type = 2
        elif any([c for c in counts.values() if c + total_jokers == 2]): # one pair
            self.type = 1
        else: # High Card
            self.type = 0
 
        self.sort_value = self.type * pow(10,10) + self.cards[0] * pow(10,8) + self.cards[1] * pow(10,6) + self.cards[2] * pow(10,4) + self.cards[3] * 100 + self.cards[4]



if __name__ == "__main__":
    input = load_input()

    hands = [Hand(l) for l in input]
    hands.sort(key=lambda hand: hand.sort_value)

    print(sum([(i + 1) * h.bid for (i, h) in enumerate(hands)]))

    hands2 = [Hand2(l) for l in input]
    hands2.sort(key=lambda hand: hand.sort_value)

    print([h._original for h in hands2])

    print(sum([(i + 1) * h.bid for (i, h) in enumerate(hands2)]))