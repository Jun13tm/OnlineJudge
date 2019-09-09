class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(nums, target):
            # Stop condition
            if len(nums) == 1:
                if nums[0] < target:
                    return 1
                else:
                    return 0
            # General case
            mid = int(len(nums)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                # Edge case: len(nums) == 2, must include nums[mid] here
                return helper(nums[mid:], target) + mid 
            else:
                return helper(nums[:mid], target)
                                    
        # Body    
        # Edge case
        if len(nums) == 0:
            return 0
        return helper(nums, target)