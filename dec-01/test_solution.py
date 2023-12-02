import pytest

import solution


@pytest.mark.parametrize(
    "line, expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("42389", 49)
    ])
def test_parse_line_part_one(line: str, expected: int) -> None:
    assert solution.parse_line_part_one(line) == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("51fp", 51),
        ("dxlb1", 11),
        ("", 0),
        ("9477", 97),
        ("t4", 44),
        ("3bqsrf", 33)
    ])
def test_parse_line_part_two(line: str, expected: int) -> None:
    assert solution.parse_line_part_two(line) == expected
