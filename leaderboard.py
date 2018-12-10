from urllib.request import Request, urlopen
from terminaltables import SingleTable
from datetime import datetime
import json
import sys

def get_content():
	req = Request('https://adventofcode.com/2018/leaderboard/private/view/33791.json')
	req.add_header('cookie', 'session=53616c7465645f5fa7aa8623cf2f8cf22426115aca9eee9bb3d63276e1ebf3766a6795d73243ec913df37609cc51fbbd')
	resp = urlopen(req)
	content = json.loads(resp.read())
	return content

def parse_content(content):
	members = content['members']
	leaderboard = {}
	for member_id,member in members.items():
		days = member['completion_day_level']
		for day,parts in days.items():
			if day not in leaderboard:
				leaderboard[day] = {1:{},2:{}}
			for part,timestamp in parts.items():
				unix_time = timestamp['get_star_ts']
				leaderboard[day][int(part)][member['name']] = int(unix_time)	
	return leaderboard

def get_table_data(leaderboard):
	data = []
	data.append(['Part 1', 'Part 2'])
	ranking = {}
	num_people = 0
	for part,people in leaderboard.items():
		sorted_times = [[k, people[k]] for k in sorted(people, key=people.get, reverse=False)]
		if part == 1:
			num_people = len(sorted_times)
		ranking[part-1] = [rank[0] for rank in sorted_times]
	for i in range(num_people):
		part_1_dude = ranking[0][i]
		if i < len(ranking[1]):
			part_2_dude = ranking[1][i]
		else:
			part_2_dude = ''
		data.append([part_1_dude, part_2_dude])
	return data

def print_table(leaderboard,day):
	data = get_table_data(leaderboard[str(day)])
	table = SingleTable(data, 'Day '+str(day))
	print(table.table)


if __name__ == '__main__':
	day = 0
	if len(sys.argv) > 1:
		day = sys.argv[1]
	content = get_content()
	leaderboard = parse_content(content)
	if day == 0:
		for i in range(1,25):
			try:
				print_table(leaderboard,i)
			except:
				break
	else:
		try:
			print_table(leaderboard,day)
		except:
			print("Unavailable")
			

	