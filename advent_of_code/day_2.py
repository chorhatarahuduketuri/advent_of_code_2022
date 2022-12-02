from advent_of_code.settings import PUZZLE_INPUT_PATH

wld = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    },
}
decode_p2_play = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z",
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    },
}

shape = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def score_game(correct_encoding: bool, p1_play: str, p2_play: str) -> int:
    if correct_encoding:
        decoded_p2_play = decode_p2_play.get(p1_play).get(p2_play)
        return wld.get(p1_play).get(decoded_p2_play) + score_shape(decoded_p2_play)
    return wld.get(p1_play).get(p2_play) + score_shape(p2_play)


def score_shape(p2_play: str) -> int:
    return shape.get(p2_play)


def compute_star_1(puzzle_input):
    return sum(
        [score_game(False, *x.split()) for x in puzzle_input.strip().split("\n")]
    )


def compute_star_2(puzzle_input):
    return sum([score_game(True, *x.split()) for x in puzzle_input.strip().split("\n")])


print("day  2, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
print("day  2, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
