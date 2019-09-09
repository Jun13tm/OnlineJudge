class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack[i:]) < len(needle):
                    return -1
                if len(needle) == 1:
                    return i
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle)-1:
                        return i
        return -1