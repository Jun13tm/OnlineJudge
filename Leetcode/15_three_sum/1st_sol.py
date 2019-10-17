class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Modified twoSum(), return all unique solutions
        def twoSum(nums, target):
            # Store pair
            dic = {}
            # Store used digits
            dic2 = {} 
            ret = []
            for i in range(len(nums)):
                if nums[i] not in dic:
                    dic[target - nums[i]] = nums[i]
                else:
                    if nums[i] not in dic2:
                        ret.append([nums[i], dic[nums[i]]])
                        dic2[nums[i]] = 1
                        dic2[dic[nums[i]]] = 1
            return ret
        
        ret = []
        dic = {}
        # Sort, very important
        nums.sort()
        for i in range(len(nums)):
            # Skip used digits
            if nums[i] not in dic:
                dic[nums[i]] = 1
                li = twoSum(nums[i + 1:], 0 - nums[i])
                if li:
                    for l in li:
                        l.append(nums[i])
                        ret.append(l)
        return ret