import pdb

def make_board(points,time):
	board = {}
	min_x = 0
	max_x = 0
	min_y = 0
	max_y = 0
	for point in points:
		position = point[0]
		velocity = point[1]
		position = [position[0]+(time*velocity[0]), position[1]+(time*velocity[1])]
		if position[0] < min_x:
			min_x = position[0]
		if position[0] > max_x:
			max_x = position[0]
		if position[1] < min_y:
			min_y = position[1]
		if position[1] > max_y:
			max_y = position[1]
		if position[0] not in board:
			board[position[0]] = {}
		board[position[0]][position[1]] = '@'

	return (max_x-min_x)*(max_y-min_y), board


def print_board(board):
	# this code is not generic. I had to adjust the size and the ranges so that I could easily see the word. 
	size = 100
	for i in range(int(size*1.25),int(size*1.75)):
		row = ''
		if i not in board:
			row = ' '*size
		else:
			for j in range(size,size*2):
				if j in board[i]:
					row += board[i][j]
				else:
					row += ' '
		print(row)



def question(input):
	points = []
	for line in input:
		position = [int(line[18:24]),int(line[10:16])]
		velocity = [int(line[40:42]),int(line[36:38])]
		points.append([position,velocity])
	time = 0
	min_area = None
	final_time = 0
	board = None
	final_board = None
	while(True):
		area, board = make_board(points,time)
		if not min_area or area <= min_area:
			min_area = area
			final_time = time
			final_board = board
		time += 1
		if time == 20000:
			break
	print_board(final_board)
	return final_time

if __name__ == '__main__':
	input = open("input.txt", "r")
	answer = question(input)
	print(answer)