import pytest

from advent_of_code import day_6

input_day_6 = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',
]
output_day_6_star_1 = [7, 5, 6, 10, 11]
# output_day_6_star_2 =

day_6_star_1_test_input = [(input_day_6, output_day_6_star_1)]
# day_6_star_2_test_input = [(input_day_6, output_day_6_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_6_star_1_test_input)
def test_day_6_star_1(puzzle_input, output):
    for i, o in zip(puzzle_input, output):
        assert day_6.compute_star_1(i) == o


# @pytest.mark.parametrize("puzzle_input, output", day_6_star_2_test_input)
# def test_day_6_star_2(puzzle_input, output):
#     assert day_6.compute_star_2(puzzle_input) == output
