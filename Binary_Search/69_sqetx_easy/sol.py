class Solution:
    def mySqrt(self, x: int) -> int:
        lower, upper = 0, x
        while 1:
            mid = int((upper - lower) / 2 + lower)
            if mid ** 2 == x:
                return mid
            else:
                if mid ** 2 < x:
                    if (mid + 1) ** 2 > x:
                        return mid
                    else:
                        lower = mid + 1
                else:
                    if (mid - 1) ** 2 <= x:
                        return mid - 1
                    else:
                        upper = mid - 1
