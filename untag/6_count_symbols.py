'''
前两题很简单，assert没搞懂，题主也没解释。最后一题“卡住”也没clarify是什么意思，但是几分钟内你肯定写得出答案。
三个非常基础的题，简单看看就行。
'''
class Solution:
	def count(self, s):
		count = 0
		for i in range(len(s)):
			if s[i] == "*":
				count += 1
		return count

	def count2(self, s):
		# set to True if bar is closed 
		closed = True
		count = 0
		for i in range(len(s)):
			if s[i] == "|":
				closed = False if closed else True
			if s[i] == "*" and closed:
				count += 1
		if closed:
			return count
		else:
			# let -1 indicate an error, or throw an exception
			return -1

	def count4(self, matrix, start_position):
		curr_position = start_position
		for i in range(len(matrix)):
			if matrix[i][curr_position] == "/":
				curr_position -= 1
			else:
				curr_position += 1
			if curr_position < 0 or curr_position >= len(matrix[0]):
				return -1
		return curr_position

if __name__ == "__main__":
	sol = Solution()

	print("Test count1")
	tests = []
	tests.append(("sfsf*bsfsf**", 3))
	tests.append(("", 0))

	for s, expected in tests:
		output = sol.count(s)
		print "string = ", s
		print "expected: ", expected, ", get: ", output
	
	print("Test count2")
	tests = []
	tests.append(("ad|fsf*sf*|", 0))
	tests.append(("ad|fsf*|sf*", 1))
	tests.append(("ad|fsf*|s|f*", -1))

	for s, expected in tests:
		output = sol.count2(s)
		print "string = ", s
		print "expected: ", expected, ", get: ", output	

	print("Test count4")
	tests = []
	tests.append(([["/", "/", "/", "/"],
					["\\", "\\", "/", "/"], 
					["\\", "\\", "\\", "\\"]], 0, -1))
	tests.append(([["/", "/", "/", "/"],
					["\\", "\\", "/", "/"], 
					["\\", "\\", "\\", "\\"]], 1, 2))
	tests.append(([["/", "/", "/", "/"],
					["\\", "\\", "/", "/"], 
					["\\", "\\", "\\", "\\"]], 2, -1))
	tests.append(([["/", "/", "/", "/"],
					["\\", "\\", "/", "/"], 
					["\\", "\\", "\\", "\\"]], 3, -1))
	for matrix, start_position, expected in tests:
		output = sol.count4(matrix, start_position)
		print "expected: ", expected, ", get: ", output	