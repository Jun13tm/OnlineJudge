'''
• Complexity:
    ○ O(n); O(n)
• Topics:
    ○ dp
判断某一格积水量：左右最高的墙壁中稍矮的那一个的高度减去当前格的高度。本题的难点在于如何将空间
复杂度降为0。naive的方法是3 pass，存两个等长的LHS,RHS array。而实际上每个格子只需要左右最高墙壁
中矮的那个高度即可，可以用two pointers实现（通常O(1)的空间复杂度，都是由Pointer实现的）。移动
较矮的那个Pointer即可（why works具体就不解释了，画个图就知道）
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

    def betterTrap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans, left_max, right_max = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return ans


