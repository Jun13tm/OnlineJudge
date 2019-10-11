class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case handling
        if len(height) <= 2: return 0
        
        left = [0] * len(height)
        right = [0] * len(height)
        
        for i in range(len(height)):
            if i == 0:
                left[i] = 0
            else:
                left[i] = max(left[i - 1], height[i - 1])
        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                right[i] = 0
            else:
                right[i] = max(right[i + 1], height[i + 1])
        # Calculation
        count = 0
        for i in range(len(height)):
            diff = min(left[i], right[i]) - height[i]
            if diff > 0:
                count += diff
        return count
    