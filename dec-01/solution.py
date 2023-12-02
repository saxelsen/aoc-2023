import re


def parse_line_part_one(line: str) -> int:
    digits = re.sub(r"\D", "", line)
    if len(digits) == 0:
        return 0
    else:
        return int(digits[0] + digits[-1])


def parse_line_part_two(line: str) -> int:
    str_to_digit_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                        "seven": "7", "eight": "8", "nine": "9"}
    regex = re.compile("|".join(str_to_digit_map.keys()), re.IGNORECASE)

    first_digit = ""
    i = 0
    while i < len(line):
        char = line[i]
        if char.isdigit():
            first_digit = char
            break
        else:
            substring = line[:i+1]
            match = regex.search(substring)
            if match:
                first_digit = str_to_digit_map[match.group(0).lower()]
                break
        i += 1

    if first_digit == "":
        return 0

    second_digit = ""
    i = -1
    while i >= -len(line):
        char = line[i]
        if char.isdigit():
            second_digit = char
            break
        else:
            substring = line[i:]
            match = regex.search(substring)
            if match:
                second_digit = str_to_digit_map[match.group(0).lower()]
                break
        i -= 1

    return int(first_digit + second_digit)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    print(sum(parse_line_part_two(line) for line in lines))