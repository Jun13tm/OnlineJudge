class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(nums, target):
            if len(nums) == 0:
                return -1
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            mid = int(len(nums)/2)
            if target >= nums[0] and target < nums[mid]:
                ret = BS(nums[:mid], target)
                return -1 if ret == -1 else ret
            else:
                ret = BS(nums[mid:], target)
                return -1 if ret == -1 else ret + mid
        
        def BSWithPivot(nums, target):
            if len(nums) == 0:
                return -1
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            
            mid = int(len(nums)/2)
            # Check if mid is the target
            if nums[mid] == target:
                return mid
            
            li_piv, li_order = [], []
            piv_offset, order_offset = 0, 0
            if nums[mid] < nums[0]:
                # Since mid is checked, don't need to include mid
                li_piv = nums[:mid]
                piv_offset = 0
                # Don't include mid for normal
                li_order = nums[mid:]
                order_offset = mid
            else: 
                # Can include mid
                li_piv = nums[mid:]
                piv_offset = mid
                li_order = nums[:mid]
                order_offset = 0
            # Check target belongs to which array
            if target >= li_order[0] and target <= li_order[-1]:
                ret = BS(li_order, target)
                return -1 if ret == -1 else ret + order_offset
            # Otherwise target in pivot list
            else:
                ret = BSWithPivot(li_piv, target)
                return -1 if ret == -1 else ret + piv_offset

        # Main
        # Handle empty array input, len(1) handled in helper functions
        if nums == []:
            return -1
        if nums[0] < nums[-1]:
            return BS(nums, target)
        else:
            return BSWithPivot(nums, target)