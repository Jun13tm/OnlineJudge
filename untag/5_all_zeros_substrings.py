#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给一个由0和1组成的string，数有多少个substring是完全由0组成的 - Solution
	"010001" -> 7 
	explanation: [0, 0, 0, 0, 00, 00, 000]
Followup:
	给一个由0和1组成的最多两行的matrix。看地里说的方法是，先把两行分别调用1维的function，再把所有列平铺开来成为一个array，
	再调用1维的function一次。感觉是一个trivial followup。

原题loop整个string，记录连续遇到多少个0，遇到1时，根据连续遇到0的数量，计算这些0提供了多少个substring。
'''
class Solution:
	def allZeroSubstrings(self, s):
		def calcSum(num_zeros):
			if self.sums[num_zeros] > -1:
				return sums[num_zeros]
			sum_ = 0
			for i in range(num_zeros + 1):
				sum_ += i
			self.sums[num_zeros] = sum_
			return sum_

		count = 0
		self.sums = [-1] * (len(s) + 1)
		num_zeros = 0
		for i in range(len(s)):
			if s[i] == '1' and num_zeros > 0:
				count += calcSum(num_zeros)
				num_zeros = 0
			if s[i] == '0':
				num_zeros += 1
		# loop ends, clear remaining num_zeros
		count += calcSum(num_zeros)
		return count

if __name__ == "__main__":
	sol = Solution()

	tests = []
	tests.append(("010001", 7))
	tests.append(("01000100", 10))
	tests.append(("", 0))

	for s, expected in tests:
		output = sol.allZeroSubstrings(s)
		print "string = ", s
		print "expected: ", expected, ", get: ", output