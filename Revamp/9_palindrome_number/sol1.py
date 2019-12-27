class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        li = [i for i in str(x)]
        i, j = 0, len(li) - 1
        while j > i:
            if li[i] != li[j]:
                return False
            i += 1
            j -= 1
        return True