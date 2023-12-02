import re


def parse_line(line: str) -> int:
    digits = re.sub(r"\D", "", line)
    if len(digits) == 0:
        return 0
    else:
        return int(digits[0]+digits[-1])


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(sum(parse_line(line) for line in lines))
