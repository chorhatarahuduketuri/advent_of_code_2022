from settings import PUZZLE_INPUT_PATH


def compute_star_1(puzzle_input):
    return sum(
        [
            ord(item) - 96 if item.islower() else ord(item) - 38
            for item in [
                set(first_compartment).intersection(set(second_compartment)).pop()
                for first_compartment, second_compartment in [
                    (
                        backpack[: len(backpack) // 2],
                        backpack[len(backpack) // 2 :],
                    )
                    for backpack in [line for line in puzzle_input.strip().split("\n")]
                ]
            ]
        ]
    )


def compute_star_2(puzzle_input):
    return sum(
        [
            ord(item) - 96 if item.islower() else ord(item) - 38
            for item in [
                set(elf_1).intersection(elf_2).intersection(elf_3).pop()
                for elf_1, elf_2, elf_3 in list(
                    zip(
                        *[iter([line for line in puzzle_input.strip().split("\n")])] * 3
                    )
                )
            ]
        ]
    )


print("day  3, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day3.txt").read()))
print("day  3, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day3.txt").read()))
