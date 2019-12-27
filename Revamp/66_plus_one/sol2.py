class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        su = 0
        digits.reverse()
        for i in range(len(digits)):
            su += 10**i * digits[i]
        su += 1
        return str(su)