
def get_total(initial_state):
	total = 0
	for i,plant in enumerate(initial_state):
		if plant == '#':
			total += (i-5)
	return total


def question_1(initial_state, conditions, generations):
	for i in range(generations):
		new_state = ['.']*len(initial_state)
		for j in range(2,len(initial_state)):
			state = ''.join(initial_state[j-2:j+3])
			if state in conditions:
				new_state[j] = conditions[state]
		if ''.join(new_state[-3:]) != '...':
			new_state.append('.')
		initial_state = new_state
	return get_total(initial_state)


def question_2(initial_state, conditions):
	after_200 = question_1(initial_state, conditions, 200)
	after_201 = question_1(initial_state, conditions, 201)
	return after_200 + (after_201-after_200)*(50000000000-200)



if __name__ == '__main__':
	initial_state = list('.....#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##.....')
	puzzle_input = open("input.txt", "r")
	conditions = {}
	for configuration in puzzle_input:
		conditions[configuration[0:5]] = configuration[9]
	answer_1 = question_1(initial_state, conditions, 20)
	print(answer_1)
	answer_2 = question_2(initial_state, conditions)
	print(answer_2)