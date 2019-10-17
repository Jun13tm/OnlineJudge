class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        # consider carry over
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
            else:
                digits[i] += 1
                return digits