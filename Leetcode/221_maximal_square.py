'''
• Complexity:
	○ O(mn); O(mn)
• Topics
	○ dp
• Related
	○ LC85 Maximal Rectangle
	○ LC363 Max Sum of Rectangle No Larger Than K
brutal force complexity为O((mn)^2)，需要找到所有的squares
dp: invaraint是：每个tile记录以该tile为右下角的square中最长的边长。所以每个tile可通过
check上面，左边和左上3个tile即可确认本tile的大小 min(up, left, upperleft) + 1
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