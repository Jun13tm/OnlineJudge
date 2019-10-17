class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(needle) > len(haystack): return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                # Now move the second pointer
                for j in range(len(needle)):
                    if haystack[j + i] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return -1
                        
                
                