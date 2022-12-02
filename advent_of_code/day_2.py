from settings import PUZZLE_INPUT_PATH

# A: X: scores 1: rock
# B: Y: scores 2: paper
# C: Z: scores 3: scissors

# loss: 0
# draw: 3
# win: 6

# win/loss/draw dicts:
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

shape = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def score_game(p1_play, p2_play) -> int:
    return wld.get(p1_play).get(p2_play)


def score_shape(p2_play: str) -> int:
    return shape.get(p2_play)


def compute_star_1(puzzle_input):
    return sum(
        [
            score_game(*x.split()) + score_shape(x[-1])
            for x in puzzle_input.strip().split("\n")
        ]
    )


print("day  2, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
