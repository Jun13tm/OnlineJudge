'''
	• Complexity:
		○ O(n); O(1)
	• Topics:
		○ dp
因为array里有负数，所以需要存prev_max和prev_min，根据实际计算结果再来更新。prev_max表示
以前一个element结尾的subarray的最大product，prev_min同理
'''
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