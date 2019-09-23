class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev_max = prev_min = overall_max = nums[0]
        for i in range(1, len(nums)):
            temp_max = prev_max * nums[i]
            temp_min = prev_min * nums[i]
            prev_max = max(temp_max, temp_min, nums[i])
            prev_min = min(temp_max, temp_min, nums[i])
            overall_max = max(overall_max, prev_max)
        return overall_max