'''
	• Complexity:
		○ O(nlogn); O(n)
	• Topics:
		○ dp
		○ binary_search
Naive dp的时间复杂度是O(n^2), 每个index记录以当前element结尾的最长subsequence:
nums: [10, 9, 2, 5, 3, 7, 101, 18]
dp:   [ 1, 1, 1, 2, 2, 3,   4,  4]

Improved dp记录的是各个长度的subsequence最佳的ending candidate，dp array自然sorted, element
应该处于的位置通过bs确定。
nums: [0, 8, 4, 12, 2]
dp:   [0]
	  [0, 8]
	  [0, 4] - 长度为2的subsequence, 4和8相比是更好的ending candidate
	  [0, 4, 12]
	  [0, 2, 12] - 长度为2的subsequence, 2和4相比是更好的candidate
Algorithm结束时，dp的长度即为最长的subsequence的长度。可以覆盖nums将space降低到O(1)
'''
class Solution:
    def naiveDP(self, nums: List[int]) -> int:
        # 注意基础长度为1
        dp = [1] * len(nums)
        # largest设置成0，应对empty input的情况
        longest = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            longest = max(longest, dp[i])
        print(dp)
        return longest

    def improvedDP(self, nums: List[int]) -> int:
        def BS(val, nums, len_dp):
            front, end = 0, len_dp - 1
            while front <= end:
                mid = (front + end) // 2
                if nums[mid] >= val:
                    # location found
                    if mid == 0 or nums[mid - 1] < val:
                        return mid
                    else:
                        end = mid - 1
                else:
                    front = mid + 1
            # loop ends naturally, val is larger than all elements in dp, append it
            return len_dp
                  
        len_dp = 0
        for i in range(len(nums)):
            idx = BS(nums[i], nums, len_dp)
            # subsitute with better candidate
            nums[idx] = nums[i]
            # only increment len_dp if appending
            if idx == len_dp:
                len_dp += 1
        return len_dp