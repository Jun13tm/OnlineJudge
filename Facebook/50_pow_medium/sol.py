class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 0: return 0

        if n < 0:
            x = 1/x
            n = -n
        prod = 1
        while n != 0:
            # if n is even
            if n % 2 == 0:
                x *= x
                n /= 2
            # otherwise do regular calculation
            else:
                prod *= x
                n -= 1
        return prod