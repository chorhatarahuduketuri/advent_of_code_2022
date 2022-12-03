import pytest

from advent_of_code import day_3

input_day_3 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
output_day_3_star_1 = 157
# output_day_3_star_2 = 45000

day_3_star_1_test_input = [(input_day_3, output_day_3_star_1)]
# day_3_star_2_test_input = [(input_day_3, output_day_3_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_3_star_1_test_input)
def test_day_3_star_1(puzzle_input, output):
    assert day_3.compute_star_1(puzzle_input) == output


# @pytest.mark.parametrize("puzzle_input, output", day_3_star_2_test_input)
# def test_day_3_star_2(puzzle_input, output):
#     assert day_3.compute_star_2(puzzle_input) == output
