print('day  1, star  1: ', max([sum([int(calorie) for calorie in line.split()]) for line in open('../puzzle_inputs/day1.txt').read().split('\n\n')]))
print('day  1, star  2: ', sum(sorted([sum([int(calorie) for calorie in line.split()]) for line in open('../puzzle_inputs/day1.txt').read().split('\n\n')], reverse=True)[:3]))
