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
def test_parse_line(line: str, expected: int) -> None:
    assert solution.parse_line(line) == expected
