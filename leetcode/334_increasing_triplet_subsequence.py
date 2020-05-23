'''
    • Complexity: 
        ○ O(n); O(1)
    • Topics: 
        ○ Array
参考k-plet的写法，array的含义是，for example，index = 4，表示所有长度的为4的increasing 
subsequence，最后一个value的最小值是多少。如果只是为了解决lc334的话，naive approach也可以
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        if not nums or len(nums) < 3:
            return False
        
        p1, p2 = nums[0], None
        
        for i in range(1, len(nums)):
            if p2 == None:
                if nums[i] > p1: 
                    p2 = nums[i]
                else: 
                    p1 = nums[i]
            # p2 set
            else:
                if nums[i] > p2: 
                    return True
                # Otherwise try update p1
                else:
                    if nums[i] > p1:
                        p2 = nums[i]
                    else:                        
                        p1 = nums[i]
        return False
        '''        
        def increasingKTriplet(nums, k):
            small_arr = [float('inf')] * (k - 1)

            for num in nums:
                for i in range(k-1):
                    if num <= small_arr[i]:
                        small_arr[i] = num
                        break

                if num > small_arr[-1]:
                    return True

            return False    
        return increasingKTriplet(nums, 3)