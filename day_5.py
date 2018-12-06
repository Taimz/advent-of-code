import string

def question_1(input):
	for line in input:
		polymer = list(line)
		i = 1
		while(True):
			previous_unit = polymer[i-1]
			unit = polymer[i]
			if unit.islower() and previous_unit.isupper() and unit.lower() == previous_unit.lower():
				del polymer[i-1:i+1]
				i -= 2
			elif unit.isupper() and previous_unit.islower() and unit.lower() == previous_unit.lower():
				del polymer[i-1:i+1]
				i -= 2
			else:
				i += 1
			if (i >= len(polymer)):
				break
		return len(polymer)	

def question_2(input):
	for line in input:
		min_value = len(line)
		alphabets = string.ascii_lowercase
		for alphabet in alphabets:
			polymer = list(line)
			j = 0
			while(True):
				unit = polymer[j]
				if unit.lower() == alphabet:
					del polymer[j]
					j -= 2
				j += 1
				if j >= len(polymer):
					break
			polymer = list(polymer)
			i = 1
			while(True):
				previous_unit = polymer[i-1]
				unit = polymer[i]
				if unit.islower() and previous_unit.isupper() and unit.lower() == previous_unit.lower():
					del polymer[i-1:i+1]
					i -= 2
				elif unit.isupper() and previous_unit.islower() and unit.lower() == previous_unit.lower():
					del polymer[i-1:i+1]
					i -= 2
				else:
					i += 1
				if i < 0:
					i = 0
				if (i >= len(polymer)):
					break
			print(alphabet + ': ' + str(len(polymer)))
			if len(polymer) < min_value:
				min_value = len(polymer)
		return min_value		



if __name__ == '__main__':
	input = open("input.txt", "r")
	# answer = question_1(input)
	answer = question_2(input)
	print(answer)