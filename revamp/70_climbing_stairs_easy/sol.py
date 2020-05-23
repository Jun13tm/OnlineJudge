class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 step corresponds to index 0
        mem = [1, 2]
        for i in range(2, n):
            mem.append(mem[i-1] + mem[i-2])
        return mem[n-1]