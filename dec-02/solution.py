import attrs
import re


@attrs.define
class Draw:
    b: int
    r: int
    g: int


@attrs.define
class Game:
    number: int
    draws: list[Draw]


class LineParsingError(Exception):
    line: str

    def __init__(self, line: str):
        self.line = line

    def __str__(self):
        return f"Could not parse line: '{self.line}'"


def parse_game(line: str) -> Game:
    match = re.match(r"Game (\d+):(.*)", line, re.IGNORECASE)

    if not match:
        raise LineParsingError(line)

    number = int(match.group(1))
    draws_string = match.group(2)
    draw_strings = draws_string.split(";")

    draws = [parse_draw(draw_string) for draw_string in draw_strings]

    return Game(number=number, draws=draws)


def parse_draw(draw_line: str) -> Draw:
    blue_match = re.search(r"(\d+) blue", draw_line, re.IGNORECASE)
    if blue_match:
        blue = int(blue_match.group(1))
    else:
        blue = 0

    red_match = re.search(r"(\d+) red", draw_line, re.IGNORECASE)
    if red_match:
        red = int(red_match.group(1))
    else:
        red = 0

    green_match = re.search(r"(\d+) green", draw_line, re.IGNORECASE)
    if green_match:
        green = int(green_match.group(1))
    else:
        green = 0

    if blue == red == green == 0:
        raise LineParsingError(draw_line)

    return Draw(b=blue, r=red, g=green)


def is_draw_possible(draw: Draw, target: Game) -> bool:
    """
    Whether the target game is possible given the draws in the source game.
    """
    for target_draw in target.draws:
        if target_draw.b > draw.b or target_draw.r > draw.r or target_draw.g > draw.g:
            return False

    return True


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()

    games = [parse_game(line) for line in lines]

    bag = Draw(b=14, r=12, g=13)
    possible_games = [game for game in games if is_draw_possible(bag, game)]
    total = sum(game.number for game in possible_games)

    print(total)