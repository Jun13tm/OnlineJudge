'''
• Complexity:
    ○ O(k) - k being the length of the repearting part
• Topics:
    ○ math - yes, pure math
    ○ hashmap
因为分母不变，那么当第一次出现重复的remainder时，意味着从decimal后第一位到当前这一位重复了。
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        
        result = []
        if numerator < 0 and denominator > 0 or numerator >= 0 and denominator < 0:
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        
        if remainder == 0: return ''.join(result)
        result.append('.')
        

        # Looking for a repeated remainder. If a remainder shows up a second time,
        # then the previous part repeat.
        d = {}
        while remainder != 0:
            if remainder in d:
                result.insert(d[remainder], '(')
                result.append(')')
                return ''.join(result)
            
            d[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
        
        return ''.join(result)