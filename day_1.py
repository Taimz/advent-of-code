
# Question 1 I just did using the delevoper tools in chrome.


def question_2():
	frequency = 0
	frequencies_reached = [0]
	input = open("input.txt", "r")
	all_frequencies = []
	for line in input:
		all_frequencies.append(int(line))
	while(True):
		for value in all_frequencies:
			frequency += value
			if frequency in frequencies_reached:
				return frequency
			frequencies_reached.append(frequency)
	return "Not found"

if __name__ == '__main__':
	answer = question_2()
	print(answer)
