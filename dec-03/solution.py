import re
import attrs


@attrs.define
class Part:
    symbols: list["Symbol"] = attrs.Factory(list)
    number: int | None = None


@attrs.define
class Symbol:
    value: str
    coords: tuple[int, int]


def puzzle_a(lines: list[str]) -> list[list[Part]]:
    parts = []

    number = ""
    part = Part()
    for y, line in enumerate(lines):
        line_parts = []
        for x, char in enumerate(line):
            if char.isdigit():
                number = number + char
                symbol = adjacent_symbol(lines, (x, y))
                if symbol is not None:
                    part.symbols.append(symbol)

            elif len(number) > 0:
                # We've reached the end of a number. Add it to the pile and reset counters.
                part.number = int(number)
                if part.symbols:
                    line_parts.append(part)
                number = ""
                part = Part()
        parts.append(line_parts)

    return parts


def adjacent_symbol(lines: list[str], x_y: [int, int]) -> Symbol | None:
    for offset_y in [-1, 0, 1]:
        search_y = x_y[1] + offset_y
        if search_y < 0 or search_y >= len(lines):
            continue

        for offset_x in [-1, 0, 1]:
            search_x = x_y[0] + offset_x

            if search_x < 0 or search_x >= len(lines[0]):
                continue

            if offset_x == 0 and offset_y == 0:
                continue

            char = lines[search_y][search_x]
            if char not in (".", "\n") and re.match(r"\D", char):
                return Symbol(value=char, coords=(search_x, search_y))

    return None


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        part_numbers = puzzle_a(lines)

        print(sum(part.number for line in part_numbers for part in line))
