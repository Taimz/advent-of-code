import datetime

#helper
def get_sleep_schedule(input):
	calendar = {}
	for line in input:
		year = int(line[1:5])
		month = int(line[6:8])
		day = int(line[9:11])
		hour = int(line[12:14])
		minute = int(line[15:17])
		date = datetime.datetime(year, month, day, hour, minute)
		action = line.split('] ')[1]
		calendar[date] = action

	guard_id = ''
	sleep_schedule = {}
	asleep_at = 0
	for key in sorted(calendar.keys()):
		action = calendar[key]
		if action.startswith('Guard'):
			guard_id = [s.split('#')[1] for s in action.split() if s.startswith('#')][0]
		elif action.startswith('falls'):
			asleep_at = key.minute
			if sleep_schedule.get(guard_id,None) is None:
				sleep_schedule[guard_id] = {
					'total_time' : 0
				}
		elif action.startswith('wakes'):
			wakes_at = key.minute
			if wakes_at < asleep_at:
				wakes_at += 60
			sleep_schedule[guard_id]['total_time'] += (wakes_at - asleep_at)
			for i in range(asleep_at,wakes_at):
				minute = i%60
				if sleep_schedule[guard_id].get(minute, None) is None:
					sleep_schedule[guard_id][minute] = 1
				else:
					sleep_schedule[guard_id][minute] += 1
	return sleep_schedule

def question_1(input):
	sleep_schedule = get_sleep_schedule(input)

	max_time = 0
	max_guard_id = ''
	for key,value in sleep_schedule.items():
		if value['total_time'] > max_time:
			max_time = value['total_time']
			max_guard_id = key
	
	max_minute_value = 0
	max_minute = 0
	for key,value in sleep_schedule[max_guard_id].items():
		if key == 'total_time':
			continue
		else:
			if value > max_minute_value:
				max_minute_value = value
				max_minute = key
	return max_minute * int(max_guard_id)


def question_2(input):
	sleep_schedule = get_sleep_schedule(input)
	
	max_minute_value = 0
	max_minute = 0
	max_guard_id = ''
	for guard_id,schedule in sleep_schedule.items():
		for minute,amount in schedule.items():
			if minute == 'total_time':
				continue
			else:
				if amount > max_minute_value:
					max_minute_value = amount
					max_minute = minute
					max_guard_id = guard_id
			
	return max_minute * int(max_guard_id)


if __name__ == '__main__':
	input = open("input.txt", "r")
	# answer = question_1(input)
	answer = question_2(input)
	print(answer)