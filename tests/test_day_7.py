import pytest

from advent_of_code import day_7

input_day_7 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
output_day_7_star_1 = 95437
output_day_7_star_2 = 24933642

day_7_star_1_test_input = [(input_day_7, output_day_7_star_1)]
day_7_star_2_test_input = [(input_day_7, output_day_7_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_7_star_1_test_input)
def test_day_7_star_1(puzzle_input, output):
    assert day_7.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_7_star_2_test_input)
def test_day_7_star_2(puzzle_input, output):
    assert day_7.compute_star_2(puzzle_input) == output
