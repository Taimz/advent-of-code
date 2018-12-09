from blist import blist

def question(marbles, num_players):
	scores = blist([0]*num_players)
	current_player = 1
	board = blist([0, 1])
	current_marble_index = 1
	for i in range(2,marbles):
		print(round(i*100/marbles,2))
		board_length = len(board)
		if i%23 != 0:
			after_index = (current_marble_index+2)%board_length
			board.insert(after_index,i)
			current_marble_index = after_index
		else:
			scores[current_player-1] += i
			other_marble_index = (current_marble_index-7)%board_length
			scores[current_player-1] += board[other_marble_index]
			del board[other_marble_index]
			current_marble_index = other_marble_index%(board_length-1)
		current_player = (current_player+1) % num_players
	return max(scores)


if __name__ == '__main__':
	num_players = 432
	part1_marbles = 71019
	part2_marbles = part1_marbles*100
	answer = question(part1_marbles, num_players)
	print(answer)