import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binaryToDecimal(a):
            su = 0
            a = [int(item) for item in a]
            a.reverse()
            for i in range(len(a)):
                su += 2**i * a[i]
            return su
        
        def decimalToBinary(a):
            if a == 0:
                return '0'
            power = int(math.log(a, 2))
            li = ['0'] * (power + 1)
            while a > 0:
                power = int(math.log(a, 2))                
                li[power] = '1'
                a -= 2**power
            li.reverse()
            return ''.join(li)     
        return decimalToBinary(binaryToDecimal(a) + binaryToDecimal(b))
