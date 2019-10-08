class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        su, dic, count = 0, {0:1}, 0

        for i in range(len(nums)): 
            su += nums[i]
            if su - k in dic:
                count += dic[su - k]
            if su not in dic:
                dic[su] = 1
            else:
                dic[su] += 1
        return count