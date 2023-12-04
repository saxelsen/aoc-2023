import re
import attrs
import copy


@attrs.define
class Card:
    number: int
    winning_numbers: list[int]
    my_numbers: list[int]

    def points(self) -> int:
        num_matches = self.num_matches()
        if num_matches == 0:
            return 0
        else:
            return 2 ** (num_matches - 1)

    def num_matches(self):
        return len(set(self.winning_numbers).intersection(self.my_numbers))


def puzzle_a(input_text: str) -> int:
    cards = parse_cards(input_text)
    return sum(card.points() for card in cards)


def parse_cards(input_text: str) -> list[Card]:
    lines = input_text.splitlines()
    return [parse_card(line) for line in lines]


def parse_card(line: str) -> Card:
    card_str, numbers_str = line.split(":")
    number = int(re.search("\d+", card_str).group())

    winning_numbers_str, my_numbers_str = numbers_str.split("|")
    winning_numbers = [int(n.strip()) for n in re.split(r"\s", winning_numbers_str.strip()) if n != ""]
    my_numbers = [int(n.strip()) for n in re.split(r"\s", my_numbers_str.strip()) if n != ""]
    return Card(number=number, winning_numbers=winning_numbers, my_numbers=my_numbers)


def puzzle_b(input_text: str) -> int:
    cards = parse_cards(input_text)

    num_cards = 0
    for card in cards:
        num_matches = card.num_matches()
        i = card.number
        for card_to_copy in cards[i : i + num_matches]:
            cards.append(copy.deepcopy(card_to_copy))
        num_cards += 1

    return num_cards


if __name__ == "__main__":
    with open("input.txt") as f:
        input_text = f.read()
    print(puzzle_a(input_text))
    print(puzzle_b(input_text))
