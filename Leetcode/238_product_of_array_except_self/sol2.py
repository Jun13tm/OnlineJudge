class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rhs = [0] * len(nums)
        # RHS
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                rhs[i] = 1
            else:
                rhs[i] = nums[i + 1] * rhs[i + 1]
        
        ret = [0] * len(nums)
        lhs = 1
        for i in range(len(nums)):
            if i == 0:
                ret[i] = lhs * rhs[i]
            else:
                lhs *= nums[i - 1]
                ret[i] = lhs * rhs[i]
        return ret
        