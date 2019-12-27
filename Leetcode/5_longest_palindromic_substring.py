'''
    • Complexity: 
        ○ O(n2); O(1) - expand from center
        ○ O(n2); O(n2) - dp
    • Topics:
        ○ palindrome
        ○ dp
    • Related
        ○ LC516 (subsequence)
Expand from center: 每一个letter，或两个letter，都尝试往左右扩张。记录一下最长的
substring的位置。
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Pay attention that this function handles two cases: a and aa
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
            return (right - left - 1, left + 1, right - 1)
        
        # Edge case handling
        if not s or len(s) <= 1: return s
        # starting/ending indices for return string
        
        ret = (0, 0, 0)
        for i in range(len(s)):
            tup1 = expand(i, i)
            tup2 = expand(i, i + 1)
            tup = tup1 if tup1[0] > tup2[0] else tup2
            
            
            if tup[0] > ret[0]: 
                ret = tup 
                
        return s[ret[1]:ret[2] + 1]