
# helper
def print_cloth(cloth):
	for key,value in cloth.items():
		line = ''
		for index,x in value.items():
			line += x
		print(line)

# helper
def count_x(cloth):
	count = 0
	for key,value in cloth.items():
		for index,x in value.items():
			if x == 'X':
				count += 1
	return count

# helper
def create_cloth():
	input = open("input.txt", "r")
	cloth = {}

	for measurement in input:
		_id = measurement.split(" @ ")[0][1:]
		info = measurement.split(" @ ")[1].split(',')
		left = int(info[0])
		the_rest = info[1].split(': ')
		top = int(the_rest[0])
		dimensions = the_rest[1].split('x')
		width = int(dimensions[0])
		height = int(dimensions[1])
		for i in range(0,top):
			if i not in cloth:
				cloth[i] = {}
			for j in range(0,left+width):
				if j not in cloth[i]:
					cloth[i][j] = '.'

		for i in range(top,top+height):
			if i not in cloth:
				cloth[i] = {}
			for j in range(0,left):
				if j not in cloth[i]:
					cloth[i][j] = '.'
			for j in range(left,left+width):
				if j in cloth[i]:
					if cloth[i][j] != '.':
						cloth[i][j] = 'X'
					else:
						cloth[i][j] = _id
				else:
					cloth[i][j] = _id
	return cloth

# helper
def find_the_full_piece(cloth):
	input = open("input.txt", "r")
	area = 0
	for measurement in input:
		_id = measurement.split(" @ ")[0][1:]
		dimensions = measurement.split(" @ ")[1].split(',')[1].split(': ')[1].split('x')
		width = int(dimensions[0])
		height = int(dimensions[1])
		area = width*height
		count = 0
		for key,value in cloth.items():
			for index,x in value.items():
				if x == _id:
					count += 1
		if count == area:
			return _id
	return 0


def question_1():
	cloth = create_cloth()
	return count_x(cloth)

def question_2():
	cloth = create_cloth()
	return find_the_full_piece(cloth)


if __name__ == '__main__':
	# answer = question_1()
	answer = question_2()
	print(answer)