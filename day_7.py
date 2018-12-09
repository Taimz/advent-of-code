import string

def question_1(input):
	instructions = {}
	reverse_instructions = {}
	for line in input:
		before = line[5]
		after = line[36]
		if after in reverse_instructions:
			reverse_instructions[after].append(before)
		else:
			reverse_instructions[after] = [before]
		if before in instructions:
			instructions[before].append(after)
		else:
			instructions[before] = [after]
	alphabets = string.ascii_uppercase
	instruction_values = instructions.values()
	starting_alphabet = 'Z'
	for alphabet in alphabets:
		alphabet_found = False
		for instruction_value in instruction_values:
			if alphabet in instruction_value:
				alphabet_found = True
				break
		if not alphabet_found:
			if alphabet <= starting_alphabet:
				starting_alphabet = alphabet
	order = [starting_alphabet]
	current_alphabet = starting_alphabet
	for i in range(0,len(alphabets)-1):
		next_alphabets = []
		if current_alphabet in instructions:
			next_alphabets = instructions[current_alphabet]
		available_alphabets = []
		unavailable_alphabets = []
		# check that all next_alphabets are available as in their keys are in order
		for alphabet in next_alphabets:
			in_order = True
			for key,value in instructions.items():
				for item in value:
					if alphabet == item:
						if key not in order and key != current_alphabet:
							in_order = False
							break
				if not in_order:
					break
			if in_order:
				available_alphabets.append(alphabet)
			else:
				unavailable_alphabets.append(alphabet)
		# for the rest, check if any alphabet has all it's keys satisfied
		if len(available_alphabets) == 0:
			for alphabet in alphabets:
				in_order = True
				for key,value in instructions.items():
					for item in value:
						if alphabet == item:
							if key not in order and key != current_alphabet:
								in_order = False
								break
					if not in_order:
						break
				if in_order:
					if alphabet not in order:
						available_alphabets.append(alphabet)
		next_alphabet = min(available_alphabets)
		order.append(next_alphabet)
		current_alphabet = next_alphabet
	return ''.join(order), reverse_instructions

def choose_next_job(worker, jobs, reverse_instructions, jobs_in_progress, workers, first_job, worker_index, current_time, jobs_done):
	# choose job.
	next_job = None
	for job in jobs:
		if job == first_job:
			next_job = job
			break
		# check if this job can be done.
		can_do_job = True
		if job in reverse_instructions:
			for instruction in reverse_instructions[job]:
				if instruction not in jobs_done:
					can_do_job = False
		if can_do_job:
			next_job = job
	if next_job:
		jobs.remove(next_job)
		jobs_in_progress.append(next_job)
		workers[worker_index]['job'] = next_job
		workers[worker_index]['start_time'] = current_time

	return jobs, reverse_instructions, jobs_in_progress, workers


def question_2(jobs, reverse_instructions):
	alphabets = string.ascii_uppercase
	workers = {}
	num_workers = 5
	for i in range(0,num_workers):
		workers[i] = {
			'job': None,
			'start_time': None
		}

	current_time = 0
	jobs_in_progress = []
	jobs_done = []
	first_job = jobs[0]
	while(True):
		# assign jobs
		for worker_index,worker in workers.items():
			worker_job = worker['job']
			worker_start_time = worker['start_time']	
			if worker_job is None:
				jobs, reverse_instructions, jobs_in_progress, workers = choose_next_job(worker, jobs, reverse_instructions, jobs_in_progress, workers, first_job, worker_index, current_time, jobs_done)
			else:
				job_duration = 60 + alphabets.index(worker_job)+1
				start_time = worker_start_time
				# if job time over
				if current_time - start_time == job_duration:
					# complete job
					workers[worker_index]['job'] = None
					workers[worker_index]['start_time'] = None
					jobs_done.append(worker_job)
					jobs_in_progress.remove(worker_job)
					jobs, reverse_instructions, jobs_in_progress, workers = choose_next_job(worker, jobs, reverse_instructions, jobs_in_progress, workers, first_job, worker_index, current_time, jobs_done)
		if len(jobs_done) == len(alphabets):
			break
		current_time += 1
		worker_jobs = [worker['job'] for worker_index,worker in workers.items()]
	return current_time


if __name__ == '__main__':
	input = open("input.txt", "r")
	jobs, reverse_instructions = question_1(input)
	print(jobs)
	answer = question_2(list(jobs), reverse_instructions)
	print(answer)