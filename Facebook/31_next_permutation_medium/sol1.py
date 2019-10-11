class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 54321 -> 12345 - reverse
        # 12345 -> 12354 -> 12435 -> 12453 -> 12534 -> 12543
        # 32451 -> 32514 -> 32541 -> 34125
        # 32543 - edge case swapping
        
        # start from rhs, the first elem that is samller than the one on its right
        # start at that index, search its rhs, find the smallest element that is 
        # larger than this one - basically when you see one that is smaller than 
        # this element, use the one to the left -> swap them
        # then sort
        
        def swap(i, j, nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            # first time
            if nums[i] < nums[i + 1]:
                # check nodes to its right
                for j in range(i + 1, len(nums)):
                    # first time
                    if nums[j] <= nums[i]:
                        swap(i, j - 1, nums)
                        break
                    if j == len(nums) - 1:
                        swap(i, j, nums)
                        break
                # sort rhs
                li = nums[i + 1:]
                li.sort()
                for j in range(i + 1, len(nums)):
                    nums[j] = li[j - i - 1]
                return
            if i == 0:
                nums.reverse()

        
        
        