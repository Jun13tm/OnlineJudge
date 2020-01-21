'''
2d matrix, two entries: "0" and "1". 0 comes before 1 in each row. Return the 
column number where the leftmost 1 appears.

Example:
	0 0 1 1 1
	0 0 0 1 1
	0 1 1 1 1
	0 0 0 1 1
Output: 1 (column index 1)

Target complexity: O(m+n) or O(mlogn) if large n 各有优劣

O(m+n)很简单，从右上角出发，如果是1则向左走，0则向下，直到到达左下角的位置。
O(mlogn):在每一层做BS，适用于较大的n。一些小tricks能加快速度。 上述例子中，
	row0在[0,4]范围内BS,找到col = 2
	row1直接check col == 2为"0"，continue
	row2 check col == 2为"1", 在[0,1]范围内BS，找到col = 1
	row3 check col == 1为"0"，触底，return col = 1
如果m很大的话，O(mlogn)趋近于O(m), 因为绝大多数的row都直接跳过了。

worst case cenario, when m is large, and matrix looks like this:
	0 0 0 0 0 1
	0 0 0 0 1 1
	0 0 0 1 1 1
	0 0 1 1 1 1
	0 1 1 1 1 1
	1 1 1 1 1 1
这种情况下是O(mlogn)，每一层都要做几乎完整的BS，此时O(m+n)就快得多。
'''

class Solution:
	# O(m+n)
	def sol1(matrix):
		if not matrix or not matrix[0]:
			return -1

		R, C = len(matrix), len(matrix[0])		
		r, c = 0, C - 1
		leftmost = C
		while r <= R - 1 and c >= 0:
			if matrix[r][c] == "0":
				if r == R - 1:
					break
				else:
					r += 1
			else:
				if c == 0:
					return 0
				else:
					leftmost = c
					c -= 1
		if leftmost == C:
			return -1
		else:
			return leftmost

		# O(mlogn)/O(nlogm)
	def sol2(matrix):
		def BS(row, front, end):
			idx = -1
			while front >= end:
				mid = (front + end) // 2
				if row[mid] == "0":
					front = mid + 1
				else row[mid] == "1":
					idx = mid
					end = mid - 1
			return idx

		if not matrix or not matrix[0]:
			return -1

		R, C = len(matrix), len(matrix[0])		
		c = C - 1
		leftmost = C

		for r in range(R):
			# Only do BS if this row is potentially better than global leftmost index
			if r[leftmost] == "1":
				curr_idx = BS(matrix[r], 0, leftmost - 1)
				if curr_idx != -1:
					leftmost = curr_idx

		if leftmost == C:
			return -1
		else:
			return leftmost