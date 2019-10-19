class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs = [0] * len(nums)
        rhs = [0] * len(nums)
        
        # LHS
        for i in range(len(nums)):
            if i == 0: 
                lhs[i] = 1
            else: 
                lhs[i] = nums[i - 1] * lhs[i - 1]
        
        # RHS
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                rhs[i] = 1
            else:
                rhs[i] = nums[i + 1] * rhs[i + 1]
        
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = lhs[i] * rhs[i]
        return ret
        