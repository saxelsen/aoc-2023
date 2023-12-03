import re
import attrs


def puzzle_a(lines: list[str]) -> list[list[int]]:
    part_numbers = []

    number = ""
    is_part_number = False

    for y, line in enumerate(lines):
        line_part_numbers = []
        for x, char in enumerate(line):
            if char.isdigit():
                number = number + char
                is_part_number = is_part_number or is_next_to_symbol(lines, (x, y))
            elif len(number) > 0:
                # We've reached the end of a number. Add it to the pile and reset counters.
                if is_part_number:
                    line_part_numbers.append(int(number))
                number = ""
                is_part_number = False
        part_numbers.append(line_part_numbers)

    return part_numbers


def is_next_to_symbol(lines: list[str], x_y: [int, int]) -> bool:
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
                return True

    return False


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        part_numbers = puzzle_a(lines)

        print(sum(num for line in part_numbers for num in line))
