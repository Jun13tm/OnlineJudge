class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Edge case
        if not s: return True
        
        # clean the string
        diff = ord('a') - ord('A')
        li = []
        for char in s:
            if ord(char) >= ord('a') and ord(char) <= ord('z'):
                li.append(char)
            elif ord(char) >= ord('0') and ord(char) <= ord('9'):
                li.append(char)
            elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
                li.append(chr(ord(char) + diff))
            else:
                continue
        i, j = 0, len(li) - 1
        while i < j:
            if li[i] != li[j]:
                return False
            i += 1
            j -= 1
        return True