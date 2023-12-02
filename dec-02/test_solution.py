import pytest

import solution
from solution import Game, Draw


@pytest.mark.parametrize("line, expected", [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
     Game(number=1, draws=[Draw(b=3, r=4, g=0), Draw(b=6, r=1, g=2), Draw(b=0, r=0, g=2)])),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
     Game(number=2, draws=[Draw(b=1, r=0, g=2), Draw(b=4, r=1, g=3), Draw(b=1, r=0, g=1)])),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
     Game(number=3, draws=[Draw(b=6, r=20, g=8), Draw(b=5, r=4, g=13), Draw(b=0, r=1, g=5)])),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
     Game(number=4, draws=[Draw(b=6, r=3, g=1), Draw(b=0, r=6, g=3), Draw(b=15, r=14, g=3)])),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
     Game(number=5, draws=[Draw(b=1, r=6, g=3), Draw(b=2, r=1, g=2)])),
])
def test_parse_game(line: str, expected: Game):
    assert solution.parse_game(line) == expected


@pytest.mark.parametrize("game, expected", [
    (Game(number=1, draws=[Draw(b=3, r=4, g=0), Draw(b=6, r=1, g=2), Draw(b=0, r=0, g=2)]), True),
    (Game(number=2, draws=[Draw(b=1, r=0, g=2), Draw(b=4, r=1, g=3), Draw(b=1, r=0, g=1)]), True),
    (Game(number=3, draws=[Draw(b=6, r=20, g=8), Draw(b=5, r=4, g=13), Draw(b=0, r=1, g=5)]), False),
    (Game(number=4, draws=[Draw(b=6, r=3, g=1), Draw(b=0, r=6, g=3), Draw(b=15, r=14, g=3)]), False),
    (Game(number=5, draws=[Draw(b=1, r=6, g=3), Draw(b=2, r=1, g=2)]), True),
])
def test_is_draw_possible(game: Game, expected: bool):
    draw = Draw(b=14, r=12, g=13)
    assert solution.is_draw_possible(draw, game) == expected


@pytest.mark.parametrize("game, expected_draw, expected_power", [
    (Game(number=1, draws=[Draw(b=3, r=4, g=0), Draw(b=6, r=1, g=2), Draw(b=0, r=0, g=2)]), Draw(r=4, g=2, b=6), 48),
    (Game(number=2, draws=[Draw(b=1, r=0, g=2), Draw(b=4, r=1, g=3), Draw(b=1, r=0, g=1)]), Draw(r=1, g=3, b=4), 12),
    (Game(number=3, draws=[Draw(b=6, r=20, g=8), Draw(b=5, r=4, g=13), Draw(b=0, r=1, g=5)]), Draw(r=20, g=13, b=6),
     1560),
    (Game(number=4, draws=[Draw(b=6, r=3, g=1), Draw(b=0, r=6, g=3), Draw(b=15, r=14, g=3)]), Draw(r=14, g=3, b=15),
     630),
    (Game(number=5, draws=[Draw(b=1, r=6, g=3), Draw(b=2, r=1, g=2)]), Draw(r=6, g=3, b=2), 36)
])
def test_smallest_possible_draw(game: Game, expected_draw: Draw, expected_power):
    smallest_draw = solution.smallest_possible_draw(game)
    assert smallest_draw == expected_draw
    assert smallest_draw.power() == expected_power
