'''
	• Complexity:
		○ O(mn)
	• Topics
		○ dp
brutal force是O((mn)^2)的complexity，naive dp(即在边长为k时，记录所有k*k的位置是不是一个
valid square，然后在边长k+1时，可以constant time check每一个k+1*k+1的square是否valid）
的complexity为O(mn^2)。Optimal Solution的dp invariant是，每个tile记录以该tile为右下角
的square，最长的边长为多少。basically，一次性检查完某一格是否存在边长为1 - n的valid square 
（对比naive dp的每个tile共检查n次）。解释起来很wordy，可以仔细看看code画图，其实不难。
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        
        max_ = 0
        for i in range(1, m + 1):
            for j in range(1 , n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if dp[i][j] > max_: max_ = dp[i][j]
        return max_ ** 2