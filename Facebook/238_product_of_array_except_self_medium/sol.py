class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # LHS
        LHS = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                LHS[i] = 1
            else:
                LHS[i] = LHS[i - 1] * nums[i - 1]
        
        # RHS
        RHS = [0] * len(nums)
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                RHS[i] = 1
            else:
                RHS[i] = RHS[i + 1] * nums[i + 1]
        
        # Final iteration
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = RHS[i] * LHS[i]
        return ret