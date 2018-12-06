import string
from difflib import SequenceMatcher


def question_1(box_ids):
	two_count = 0
	three_count = 0
	alphabets = string.ascii_lowercase
	for word in box_ids:
		two_count_present = False
		three_count_present = False
		for alphabet in alphabets:
			count = word.count(alphabet)
			if count == 2:
				two_count_present = True
			elif count == 3:
				three_count_present = True
		if two_count_present:
			two_count += 1
		if three_count_present:
			three_count += 1
	return two_count * three_count


def question_2(box_ids):
	word_a = ""
	word_b = ""
	for word in box_ids:
		for to_match in box_ids:
			ratio = SequenceMatcher(a=word,b=to_match).ratio()
			if ratio > 0.95 and ratio < 1:
				word_a = word
				word_b = to_match

	final_word = ''
	for i in range(0,len(word_a)):
		if word_a[i] == word_b[i]:
			final_word += word_a[i]
			
	return final_word



if __name__ == '__main__':
	input = open("input.txt", "r")
	box_ids = []
	for line in input:
		box_ids.append(line)
	# answer = question_1(box_ids)
	answer = question_2(box_ids)
	print(answer)