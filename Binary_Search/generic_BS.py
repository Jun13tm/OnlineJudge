def BS(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    mid = int(len(nums)/2)
    # In case array has only two elements, must exclude second element
    # e.g. nums = [0,1]; target = 0, exclude 1 or will stuck with [0,1] 
    if target >= nums[0] and target < nums[mid]:
        ret = BS(nums[:mid], target)
        return -1 if ret == -1 else ret
    # It's okay to include mid here (>= case)
    # e.g. nums = [0,1]; target = 1, use [1] in next iteration
    else:
        ret = BS(nums[mid:], target)
        return -1 if ret == -1 else ret + mid