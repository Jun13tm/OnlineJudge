'''
    • Complexity
        ○ O(n2) - so sorting doesn't affect time-complexity
    • Topics
        ○ sort
        ○ two_pointers (kind of)
call two_sum()多次，记录所有结果。重点在于先sort->因此可以跳过repeated digit (因为first 
occurrence已经记录了所有pair)。注意two_sum里要handle duplicates，因此用set储存valid pairs。
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Modified twoSum(), return all unique solutions
        # Set is used to store unique solutions e.g. [-1,1,1]
        def twoSum(li, target):
            dic = {}
            set_ = set()
            for i in range(len(li)):
                if li[i] in dic:
                    set_.add((dic[li[i]], li[i]))
                else:
                    dic[target - li[i]] = li[i]                
            ret = []
            for x, y in set_:
                ret.append([x, y])
            return ret
        
        ret = []
        dic = {}
        # Sort, very important
        nums.sort()
        for i in range(len(nums)):
            # Skip repeated digits, so no duplicates to handle.
            if nums[i] not in dic:
                dic[nums[i]] = 1
                li = twoSum(nums[i + 1:], 0 - nums[i])
                for l in li:
                    l.append(nums[i])
                    ret.append(l)
        return ret
                