
def define_power_levels(serial_number):
	power_levels = []
	for i in range(1,301):
		row = []
		for j in range(1,301):
			rack_id = i+10
			power_level = (((rack_id)*j)+serial_number)*rack_id
			hundreds_number = int((power_level/100)%10)
			if hundreds_number < 1:
				hundreds_number = 0
			final_power_level = hundreds_number-5
			row.append(final_power_level)
		power_levels.append(row)
	return power_levels

def get_coordinates(power_levels, size):
	max_power = 0
	coordinates = ''
	for i in range(0,300):
		if i > (300-size):
			continue
		for j in range(0,300):
			if j > (300-size):
				continue
			power = 0
			for k in range(0,size):
				for l in range(0,size):
					power += power_levels[i+k][j+l]
			if power > max_power:
				max_power = power
				coordinates = str(i+1)+','+str(j+1)
	return coordinates, max_power


def question_1(serial_number):
	power_levels = define_power_levels(serial_number)	
	size = 3
	return get_coordinates(power_levels, size)
	
def question_2(serial_number):
	power_levels = define_power_levels(serial_number)
	max_power = 0
	max_coordinates = ''
	max_size = 0
	same_for = 0
	for size in range(300):
		if same_for > 5:
			break
		coordinates, power = get_coordinates(power_levels,size)
		if power > max_power:
			max_power = power
			max_coordinates = coordinates
			max_size = size
		else:
			same_for += 1
	return max_coordinates, max_size, max_power


if __name__ == '__main__':
	serial_number = 7511
	coordinates, power = question_1(serial_number)
	print('Answer 1: ' + str(coordinates))
	coordinates, size, power = question_2(serial_number)
	print('Answer 2: ' + str(coordinates) + ',' + str(size))

