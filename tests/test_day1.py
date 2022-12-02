import pytest

from advent_of_code import day_1

input_day_1 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
output_day_1_star_1 = 24000
output_day_1_star_2 = 45000

day_1_star_1_test_input = [(input_day_1, output_day_1_star_1)]
day_1_star_2_test_input = [(input_day_1, output_day_1_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_1_star_1_test_input)
def test_day_1_star_1(puzzle_input, output):
    assert day_1.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_1_star_2_test_input)
def test_day_1_star_2(puzzle_input, output):
    assert day_1.compute_star_2(puzzle_input) == output
