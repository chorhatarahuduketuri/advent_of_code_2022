import pytest

from advent_of_code import day_5

input_day_5 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
output_day_5_star_1 = "CMZ"
# output_day_5_star_2 =

day_5_star_1_test_input = [(input_day_5, output_day_5_star_1)]
# day_5_star_2_test_input = [(input_day_5, output_day_5_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_5_star_1_test_input)
def test_day_5_star_1(puzzle_input, output):
    assert day_5.compute_star_1(puzzle_input) == output


# @pytest.mark.parametrize("puzzle_input, output", day_5_star_2_test_input)
# def test_day_5_star_2(puzzle_input, output):
#     assert day_5.compute_star_2(puzzle_input) == output
