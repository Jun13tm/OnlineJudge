def occurrence(a):
	# O(n^2) - iterate all digits in all items in list a
	# No negative value / no empty array, so no handling
	count = 0
	for item in a:
		li = list(str(item))
		is_odd = False
		for digit in li:
			if digit == '0':
				is_odd = True if is_odd == False else False
		if is_odd: 
			count += 1
	return count

def cyclic_shift(elements):
	# O(n)
	# Double elements array方便处理end traverse到front这个过程
	if not elements or len(elements) == 0:
		return False

	idx = elements.index(1)
	double = elements * 2
	failed = False
	# Increasing order
	for i in range(len(elements)):
		if double[idx + i] != i + 1:
			failed = True
			break
	if failed:
		# Decreasing order
		idx += len(elements)
		for i in range(len(elements)):
			if double[idx - i] != i + 1:
				return False
	return True

def pair_power_of_two(a):
	# O(n^2)
	# 写完了才发现是distinct integer，这个写法在有duplicate的时候会更快。check是否是2的power
	# 复杂度是O(1)。 
	if a is None: return 0

	powers, mp = {1}, 1
	counts = [0] * len(a)

	for i in range(len(a) - 1, -1, -1):
		for j in range(i, len(a)):
			if j > i and a[j] == a[i]:
				counts[i] += counts[j]
				break
			# Check if sum gives power of 2
			s = a[i] + a[j]
			while s > mp:
				mp = pow(2, len(powers))
				powers.add(mp)
			if s in powers:
				counts[i] += 1
	return sum(counts)

def city(m, n, start, target):
	# Worst case? O(m*n) * 4, assume x1, x2, y1, y2 are all in range
	curr, direct = start, (1, 1)
	history = {curr + direct}
	steps = 0
	while True:
		steps += 1
		ne = (curr[0] + direct[0], curr[1] + direct[1])
		ne_direct = (direct[0], direct[1])
		if ne[0] > m or ne[0] < 0:
			ne_direct = (ne_direct[0] * -1, ne_direct[1])
		if ne[1] > n or ne[1] < 0:
			ne_direct = (ne_direct[0], ne_direct[1] * -1)
		if ne_direct == direct:
			curr = ne
		else:
			direct = ne_direct

		if curr == target:
			return steps
		if (curr + direct) in history:
			return -1
		else:
			history.add(curr + direct)

def falling_matrix(matrix): 
	# O(m*n)
	fall = float('inf')
	loc = [None] * len(matrix[0])
	blocks = set()
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			cell = matrix[r][c]
			if cell == 'F':
				loc[c]= r
			if cell == '#':
				blocks.add((r, c))
				if loc[c] is not None:
					fall = min(r - loc[c] - 1, fall)
					loc[c] = None
		# Treat bottom as blocks
		if r == len(matrix) - 1:
			for c in range(len(matrix[r])):
				if loc[c] is not None:
					fall = min(r - loc[c], fall)
	# Generate output matrix based on fall
	if fall == 0:
		return matrix
	for co in blocks:
		matrix[co[0]][co[1]] = '.'
	after = [[None] * len(matrix[0])] * len(matrix)
	for r in range(len(after)):
		if r < fall:
			after[r] = ['.'] * len(matrix[0])
		else:
			# This is shallow copy
			after[r] = matrix[r - fall]
	for co in blocks:
		after[co[0]][co[1]] = '#'
	return after

class Node:
	def __init__(self, val):
		self.neighbors = []
		self.val = val

def corrupted_array(pairs):
	# O(n)
	dic = {}
	for v1, v2 in pairs:
		n1 = dic[v1] if v1 in dic else Node(v1)
		dic[v1] = n1
		n2 = dic[v2] if v2 in dic else Node(v2)
		dic[v2] = n2
		n1.neighbors.append(n2)
		n2.neighbors.append(n1)

	for v in dic:
		if len(dic[v].neighbors) == 1:
			break
	restored = [v]
	prev, curr = dic[v], dic[v].neighbors[0]
	while len(curr.neighbors) > 1:
		restored.append(curr.val)
		for n in curr.neighbors:
			if prev != n:
				prev = curr
				curr = n
				# Must break here since curr is re-assigned
				break
	return restored + [curr.val]

def main():
	a = [4, 50, 100, 65, 2000, 700, 1, 10]
	assert occurrence(a) == 3
	a = [20, 11, 10, 10070, 7]
	assert occurrence(a) == 3

	elements = [1, 4, 2, 3]
	assert cyclic_shift(elements) == False
	elements = [4, 3, 2, 1]
	assert cyclic_shift(elements) == True
	elements = [2, 3, 4, 1]
	assert cyclic_shift(elements) == True

	a = [1, -1, 2, 3]
	assert pair_power_of_two(a) == 5
	a = [1, 1, 2, 3]
	assert pair_power_of_two(a) == 6
	a = [1]
	assert pair_power_of_two(a) == 1

	m, n, start, target = 3, 3, (2, 2), (1, 1)
	assert city(m, n, start, target) == 4
	m, n, start, target = 3, 3, (2, 2), (1, 2)
	assert city(m, n, start, target) == -1
	m, n, start, target = 3, 3, (2, 1), (1, 3)
	assert city(m, n, start, target) == -1

	matrix = [
		['F', 'F', 'F'],
		['.', 'F', '.'],
		['.', 'F', 'F'],
		['#', 'F', '.'],
		['F', 'F', '.'],
		['.', '.', '.'],
		['.', '.', '#'],
		['.', '.', '.']
	]
	expected = [
		['.', '.', '.'],
		['.', '.', '.'],
		['F', 'F', 'F'],
		['#', 'F', '.'],
		['.', 'F', 'F'],
		['.', 'F', '.'],
		['F', 'F', '#'],
		['.', '.', '.']
	]
	assert falling_matrix(matrix) == expected

	pairs = [[3, 5], [1, 4], [2, 4], [1, 5]]
	restored = corrupted_array(pairs)
	if restored == [3, 5, 1, 4, 2] or restored == [2, 4, 1, 5, 3]:
		assert True
	else:
		assert False

	print('All passed')

if __name__ == "__main__":
	main()