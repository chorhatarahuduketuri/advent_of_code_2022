from settings import PUZZLE_INPUT_PATH


def compute_star_1(puzzle_input):
    return sum(
        [
            (
                pair_of_elves[0][0] <= pair_of_elves[1][0]
                and pair_of_elves[0][1] >= pair_of_elves[1][1]
            )
            or (
                pair_of_elves[1][0] <= pair_of_elves[0][0]
                and pair_of_elves[1][1] >= pair_of_elves[0][1]
            )
            for pair_of_elves in [
                [
                    [int(position) for position in assignment.split("-")]
                    for assignment in pair
                ]
                for pair in [
                    line.split(",") for line in puzzle_input.strip().split("\n")
                ]
            ]
        ]
    )


def compute_star_2(puzzle_input):
    return


print("day  4, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day4.txt").read()))
# print("day  4, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day4.txt").read()))
