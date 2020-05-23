class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return None
        
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)
        for i in range(k):
            ret = heapq.heappop(nums)
        return ret * -1