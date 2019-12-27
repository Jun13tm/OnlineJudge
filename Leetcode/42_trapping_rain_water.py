'''
• Complexity:
    ○ O(n); O(n)
• Topics:
    ○ dp
判断某一格积水量：左右最高的墙壁中稍矮的那一个的高度减去当前格的高度
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # LHS
        LHS = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                LHS[i] = 0
            else:
                LHS[i] = max(height[i - 1], LHS[i - 1])
        
        # RHS
        RHS = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                RHS[0] = 0
            else:
                RHS[i] = max(height[i + 1], RHS[i + 1])
        
        count = 0
        for i in range(len(height)):
            diff = min(LHS[i], RHS[i]) - height[i]
            if diff > 0: count += diff
        return count