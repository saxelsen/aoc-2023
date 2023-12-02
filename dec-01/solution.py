import re


def parse_line_part_one(line: str) -> int:
    digits = re.sub(r"\D", "", line)
    if len(digits) == 0:
        return 0
    else:
        return int(digits[0] + digits[-1])


def parse_line_part_two(line: str) -> int:
    first_digit = _extract_digit(line, reverse=False)

    if first_digit == "":
        return 0

    second_digit = _extract_digit(line, reverse=True)

    return int(first_digit + second_digit)


def _extract_digit(line: str, reverse=False) -> str:
    str_to_digit_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                        "seven": "7", "eight": "8", "nine": "9"}
    regex = re.compile("|".join(str_to_digit_map.keys()), re.IGNORECASE)

    i = 0 if not reverse else -1
    loop_iteration = i if not reverse else -i
    # when going in reverse the loop_iteration counter starts at 1 so we have to extend the length
    max_iterations = len(line) if not reverse else len(line) + 1

    digit = ""
    while loop_iteration < max_iterations:
        char = line[i]
        if char.isdigit():
            digit = char
            break
        else:
            substring = line[:i+1] if not reverse else line[i:]
            match = regex.search(substring)
            if match:
                digit = str_to_digit_map[match.group(0).lower()]
                break
        i = i + 1 if not reverse else i - 1
        loop_iteration = i if not reverse else -i

    return digit


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    print(sum(parse_line_part_two(line) for line in lines))
