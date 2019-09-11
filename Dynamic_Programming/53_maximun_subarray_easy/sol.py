class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        consec_max = [nums[0]]
        overall_max = nums[0]
        for i in range(1, len(nums)):
            consec_max.append(max(nums[i], consec_max[i-1] + nums[i]))
            overall_max = max(consec_max[i], overall_max)
        return overall_max