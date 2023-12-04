import re
import attrs

symbols: dict[tuple[int, int, str], "Symbol"] = {}


@attrs.define
class Part:
    symbols: set["Symbol"] = attrs.Factory(set)
    number: int | None = None

    def __eq__(self, other):
        if not isinstance(other, Part):
            return False

        return self.number == other.number

    def __hash__(self):
        return hash(self.number)


@attrs.define
class Symbol:
    value: str
    coords: tuple[int, int]
    parts: list[Part] = attrs.Factory(list)

    def get_parts(self):
        return set(self.parts)

    def __eq__(self, other):
        if not isinstance(other, Symbol):
            return False

        return self.value == other.value and self.coords == other.coords

    def __hash__(self):
        return hash((self.value, self.coords))


def puzzle_a(lines: list[str]) -> int:
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
                    part.symbols.add(symbol)
                    symbol.parts.append(part)

            elif len(number) > 0:
                # We've reached the end of a number. Add it to the pile and reset counters.
                part.number = int(number)
                if part.symbols:
                    line_parts.append(part)
                number = ""
                part = Part()
        parts.append(line_parts)

    return sum(part.number for line in parts for part in line)


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
                # Look up the symbol to see if we have encountered it before,
                # otherwise create a new one and store it.
                try:
                    symbol = symbols[(search_x, search_y, char)]
                except KeyError:
                    symbol = Symbol(value=char, coords=(search_x, search_y))
                    symbols[(search_x, search_y, char)] = symbol
                return symbol

    return None


def puzzle_b() -> int:
    if not symbols:
        raise Exception("Run puzzle_a first")

    gears = []
    for symbol in symbols.values():
        if symbol.value == "*":
            if len(symbol.get_parts()) == 2:
                gears.append(symbol)

    gear_ratios = []
    for gear in gears:
        parts = list(gear.get_parts())
        assert len(parts) == 2, "Gears should have 2 parts"
        gear_ratio = parts[0].number * parts[1].number
        gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()

    part_numbers = puzzle_a(lines)

    # puzzle A answer
    print(puzzle_a(lines))
    print(puzzle_b())
