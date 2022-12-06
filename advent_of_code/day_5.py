from settings import PUZZLE_INPUT_PATH


def setup_stacks_from_initial_position(initial_position: str):  # -> list[list[str]]:
    input_lines = [line for line in initial_position.split("\n")]
    stacks = [
        []
        for stack in range(
            max([int(stack_number) for stack_number in input_lines.pop().split()])
        )
    ]
    # Don't say I didn't warn you about the really disgusting abuse of list comprehensions....
    [
        [
            stacks[stack].append(crate)
            for stack, crate in enumerate(layer[1::4])
            if crate.strip()
        ]
        for layer in input_lines[::-1]
    ]
    return stacks


def execute_moves(stacks: list[list[str]], moves: str) -> list[list[str]]:
    rearrangement_procedure = [
        [int(number) for number in move.split()[1::2]] for move in moves.split("\n")
    ]
    [
        [
            stacks[operation[2] - 1].append(stacks[operation[1] - 1].pop())
            for op in range(operation[0])
        ]
        for operation in rearrangement_procedure
    ]
    return stacks


def compute_star_1(puzzle_input):
    initial_position, moves = puzzle_input.rstrip().split("\n\n")
    stacks = setup_stacks_from_initial_position(initial_position)
    stacks = execute_moves(stacks, moves)
    return "".join([stack[-1] for stack in stacks])


# def compute_star_2(puzzle_input):
#     return


print("day  5, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
# print("day  5, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
