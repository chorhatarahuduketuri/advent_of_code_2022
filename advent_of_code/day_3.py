from settings import PUZZLE_INPUT_PATH


def compute_star_1(puzzle_input):
    return sum([ord(item)-96 if item.islower() else ord(item)-64 for item in [set(first_compartment).intersection(set(second_compartment)).pop() for first_compartment, second_compartment in [(backpack[:len(backpack)//2], backpack[len(backpack)//2:],) for backpack in [line for line in puzzle_input.strip().split('\n')]]]])


# def compute_star_2(puzzle_input):
#     return


print("day  3, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day3.txt").read()))  # 3820 too low
# print("day  3, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day3.txt").read()))
