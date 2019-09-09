class Solution:
    def reverse(self, x: int) -> int:
        is_neg = -1
        if x < 0:
            is_neg = 1
        x = abs(x)
        li = [int(x) for x in str(x)]
        li.reverse()
        index = len(li)-1
        su = 0
        for digit in li:
            su += digit*10**index
            index -= 1
        if is_neg == 1:
            if su > 2**31:
                return 0
            return su * -1
        else:
            if su > 2**31-1:
                return 0
            return su