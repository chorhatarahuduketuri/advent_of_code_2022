import pytest

from advent_of_code import day_4

input_day_4 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
output_day_4_star_1 = 2
output_day_4_star_2 = 4

day_4_star_1_test_input = [(input_day_4, output_day_4_star_1)]
day_4_star_2_test_input = [(input_day_4, output_day_4_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_4_star_1_test_input)
def test_day_4_star_1(puzzle_input, output):
    assert day_4.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_4_star_2_test_input)
def test_day_4_star_2(puzzle_input, output):
    assert day_4.compute_star_2(puzzle_input) == output
