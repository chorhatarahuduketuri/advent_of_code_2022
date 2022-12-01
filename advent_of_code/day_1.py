from settings import PUZZLE_INPUT_PATH


def compute_star_1(puzzle_input):
    return max(
        [
            sum([int(calorie) for calorie in line.split()])
            for line in puzzle_input.split("\n\n")
        ]
    )


def compute_star_2(puzzle_input):
    return sum(
        sorted(
            [
                sum([int(calorie) for calorie in line.split()])
                for line in puzzle_input.split("\n\n")
            ],
            reverse=True,
        )[:3]
    )


print("day  1, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
print("day  1, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
