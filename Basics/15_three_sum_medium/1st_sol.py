class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSumHelper(nums, target):
            ret = []
            dic = {}
            for i in range(len(nums)):
                # Check if current number has been included in a valid pair.
                if nums[i] in dic and dic[nums[i]] == -1:
                    continue
                if target-nums[i] not in dic:
                    dic[nums[i]] = i
                else:
                    if dic[target-nums[i]] == -1:
                        continue
                    li = [target-nums[i], nums[i]]
                    ret.append(li)
                    dic[target-nums[i]] = -1
            return ret

        # Since runtime will be in O(n^2), sort doesn't cost a lot
        nums.sort()
        ret = []
        dic = {}
        print(nums)
        for i in range(len(nums)):
            if nums[i] in dic:
                continue
            dic[nums[i]] = 1
            pairs = twoSumHelper(nums[i+1:], 0-nums[i])