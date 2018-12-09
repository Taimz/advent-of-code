
def question_1(license_file):
	tree = {}
	# states: 0 = store child nodes quantity, 1 = store metadata quantity, 2 = metadata values
	state = 0
	kids = [0]
	level = 0
	node_number = 1
	child_assembly_number = 2
	parent = 0
	nodes_made = 0
	for value in license_file:
		if state == 0:
			tree[node_number] = {'num_nodes': value, 'num_metadata': 0, 'metadata': [], 'children':[child_assembly_number+i for i in range(0,value)], 'parent': parent, 'level': level}
			child_assembly_number += value
			state = 1
			nodes_made += 1
		elif state == 1:
			tree[node_number]['num_metadata'] = value
			if tree[node_number]['num_nodes'] == 0:
				state = 2
			else:
				level += 1
				parent = node_number
				if len(kids) > level:
					kids[level] = tree[node_number]['num_nodes']
				else:
					kids.append(tree[node_number]['num_nodes'])
				state = 0
				node_number += 1
		elif state == 2:
			num_metadata = tree[node_number]['num_metadata']
			if num_metadata != 0:
				tree[node_number]['metadata'].append(value)				
				tree[node_number]['num_metadata'] -= 1
			if tree[node_number]['num_metadata'] == 0:
				kids[level] -= 1
				if kids[level] == 0:
					level -= 1
					node_number = tree[node_number]['parent']
				else:
					state = 0
					parent = tree[node_number]['parent']
					node_number = nodes_made+1
	answer = 0
	for node_number,data in tree.items():
		answer += sum(tree[node_number]['metadata'])
	return answer



def traverse(tree):
	child_nodes = tree[0]
	metadata = tree[1]
	del tree[0:2]

	values = []

	for i in range(0,child_nodes):
		value, tree = traverse(tree)
		# store values of child nodes in order
		values.append(value)

	if child_nodes == 0:
		metadata_values = tree[0:metadata]
		the_value = sum(metadata_values)
		del tree[0:metadata]
		return the_value, tree
	else:
		the_value = 0
		for i in tree[0:metadata]:
			# to make sure index doesn't go out of bounds of available child nodes
			if i <= len(values):
				the_value += values[i - 1]
		del tree[0:metadata]
		return the_value, tree
		

def question_2(tree):
	value, tree = traverse(tree)
	return value



if __name__ == '__main__':
	input = open("input.txt", "r")
	license_file = ''
	for line in input:
		license_file = line.split()
	license_file = [int(value.strip()) for value in license_file]
	# answer = question_1(license_file)
	answer = question_2(license_file)
	print(answer)



