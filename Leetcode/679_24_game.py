'''
• Complexity: 
	○ O(1); O(1)
• Topics:
	○ complex loop
	○ combinatorics
忽略括号，一共有4种cards（忽略value），4种Opearators（其中 - 和 //的order matter，+ 和 * don't matter）
那么我们需要做的就是对每组input，计算所有的calculation permutation，判断是否有任意一个permutation得到24。
按照如下步骤：
	1. 4 cards choose 2，由于2个operators要求order matter，e.g. 2//1 != 1//2，所以用Permutation: 4P2 = 4!/(4-2)! = 12
	2. 4 operators choose 1，并在这上面两张卡中执行，合并成一张新卡。operator order doesn't matter，4种可能性
	3. 3 cards choose 2(包括了新生成的1张卡，和2张未选用的卡），Permutation: 3P2 = 3!/(3-2)! = 6 
	4. 4 operators choose 1, 在上面两张卡中执行，合并成一张新卡。4种可能性
	5. 2 cards choose 2(包括了新生成的1张卡，和1张未选用的卡），Permutation: 2P2 = 2!/(2-1)! = 2 
	6. 4 operators choose 1, 在上面两张卡中执行，输出最后的结果。4种可能性
Total number of combined permutations: 12*4*6*4*2*4 = 9,216 
9216设置了计算数量的upper bound（因为+和* 不受顺序影响，可以省略几次计算）。如下写法虽然很niche，但值得学习。
'''
from operator import truediv, mul, add, sub

class Solution(object):
	def judgePoint24(self, A):
		if not A: return False

		# recursion base case, this should store the final calculation result of this permutation
		if len(A) == 1:
            # yes you are right, we cannot directly compare to 0, consider [3,3,8,8]
            # why abs()? consider [1,2,1,2]
			return abs(A[0] - 24) < 1e-6

		# Step1: 4 cards choose 2
		for i in range(len(A)):
			for j in range(len(A)):
				if i != j:
					# group the two unchosen elements in list B, here k != i and k != j
					B = [A[k] for k in range(len(A)) if i != k != j]
					# Step2: 4 opeartors choose 1, calculate, push to B
					for op in (truediv, mul, add, sub):
                        # optional, for this two operators, i > j calculation duplicates
						if (op is add or op is mul) and j > i: continue
                        # might div by zero, check A[j] != 0 when truediv
						if op is not truediv or A[j]:
							B.append(op(A[i], A[j]))
							# now it becomes a 3-cards sub-problem, call this function again
							# if recursion returns True, then this permuation gives 24, return True
							if self.judgePoint24(B): return True
							# otherwise, pop the new card, choose another opearator
							B.pop()
		# All combination failed
		return False