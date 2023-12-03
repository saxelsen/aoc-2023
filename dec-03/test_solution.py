import solution


def test_solution_puzzle_a():
    input = ("467..114..\n"
             "...*......\n"
             "..35..633.\n"
             "......#...\n"
             "617*......\n"
             ".....+.58.\n"
             "..592.....\n"
             "......755.\n"
             "...$.*....\n"
             ".664.598..\n"
             )

    lines = input.splitlines()

    assert sum(solution.puzzle_a(lines)) == 4361
