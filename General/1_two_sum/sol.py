# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
        	# if complement is not in dict, add current number in dict
            if target-nums[i] not in dic:
                dic[nums[i]]=i
            else:
                return [dic[target-nums[i]],i]