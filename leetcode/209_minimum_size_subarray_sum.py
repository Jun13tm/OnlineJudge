'''
    • Complexity:
        ○ O(n)
    • Topics
        ○ sliding_window
    • Related
        ○ untag 4: 1d largest land
 和Untag4类似，front和end指向同一个index时，front会移动到end右边，并记录此时长度为1。和
 untag4相比，检查更新ans的位置不同。
'''
class solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        front, sum_, ans = 0, 0, float("inf")
        
        for end in range(len(nums)):
            while sum_ + nums[end] >= s:
                ans = min(ans, end - front + 1)
                sum_ -= nums[front]
                front += 1
            sum_ += nums[end]
        if ans == float("inf"):
            return 0
        else:
            return ans