import re
import attrs


@attrs.define
class Card:
    number: int
    winning_numbers: list[int]
    my_numbers: list[int]

    def points(self) -> int:
        intersection = set(self.winning_numbers).intersection(self.my_numbers)
        if len(intersection) == 0:
            return 0
        else:
            return 2 ** (len(intersection) - 1)


def puzzle_a(input_text: str) -> int:
    lines = input_text.splitlines()
    cards = []
    for line in lines:
        card = parse_card(line)
        cards.append(card)

    return sum(card.points() for card in cards)


def parse_card(line: str) -> Card:
    card_str, numbers_str = line.split(":")
    number = int(re.search("\d+", card_str).group())

    winning_numbers_str, my_numbers_str = numbers_str.split("|")
    winning_numbers = [int(n.strip()) for n in re.split(r"\s", winning_numbers_str.strip()) if n != ""]
    my_numbers = [int(n.strip()) for n in re.split(r"\s", my_numbers_str.strip()) if n != ""]
    return Card(number=number, winning_numbers=winning_numbers, my_numbers=my_numbers)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_text = f.read()
    print(puzzle_a(input_text))
