from settings import PUZZLE_INPUT_PATH


def compute_star_1(puzzle_input):
    return [
        i
        for i in [
            index + 4 if len(set(puzzle_input[index : index + 4])) == 4 else None
            for index, char in enumerate(puzzle_input)
            if index < len(puzzle_input.strip())
        ]
        if i is not None
    ][0]


# def compute_star_2(puzzle_input):
#     return


print(
    "day  6, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day6.txt").read())
)  # print("day  6, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day6.txt").read()))
