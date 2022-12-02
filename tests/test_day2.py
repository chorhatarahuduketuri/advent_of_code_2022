import pytest

from advent_of_code import day_2

input_day_2 = """A Y
B X
C Z"""
output_day_2_star_1 = 15
output_day_2_star_2 = 12

day_2_star_1_test_input = [(input_day_2, output_day_2_star_1)]
day_2_star_2_test_input = [(input_day_2, output_day_2_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_2_star_1_test_input)
def test_day_2_star_1(puzzle_input, output):
    assert day_2.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_2_star_2_test_input)
def test_day_2_star_2(puzzle_input, output):
    assert day_2.compute_star_2(puzzle_input) == output
