'''
1d verison: list of lands with prices and a max budge, return largest size of contiguous lands.

Example:
input: [1, 1, 3, 2, 4, 3, 2], budget = 7
output: 4
explanation: [1, 1, 3, 2] <= 7

Follow-up: 
2d version: 2d matrix of lands, return largest square land under the budget

Example:
input: [[1, 1, 3, 2, 4, 3, 2]
		[1, 1, 3, 2, 4, 3, 2]
		[1, 1, 3, 2, 4, 3, 2]] 
		budget = 4
output: 2
explanation:
	[[1, 1]
	 [1, 1]]


1d version:
end跳过所有价格超过budget的地。如果买不起当前的地，keep moving front to the right，直到
能买的起当前的地为止。注意，front指向的位置已经被买下，每个iteration，end指向的地尚未正要
被evaluate，但还未购买。注意不能用end - front去记录Curr_length，之间可能有超过budget的地。

2d version:



'''
class Solution:
	def largestLand1D(self, lands, budget):
		front, expense, curr_length, largest = -1, 0, 0, 0

		for end in range(len(lands)):
			if lands[end] > budget:
				continue
			else:
				while expense + lands[end] > budget:
					if lands[front] <= budget and front > -1:
						expense -= lands[front]
						curr_length -= 1	
					front += 1
				# Now can purchase current land
				expense += lands[end]
				curr_length += 1
				largest = max(largest, curr_length)
		return largest

	def largestLand2D(self, lands, budget):


if __name__ == "__main__":
	sol = Solution()

	tests = []
	tests.append(([1, 1, 3, 2, 4, 3, 2], 7, 4))
	tests.append(([8, 8, 2], 7, 1))
	tests.append(([1,1,3,2,8,8,3,2], 7, 4))

	for lands, budget, expected in tests:
		output = sol.largestLand1D(lands, budget)
		print lands, "budget = ", budget
		print "expected: ", expected, ", get: ", output