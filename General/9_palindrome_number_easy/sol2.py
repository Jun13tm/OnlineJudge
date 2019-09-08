class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        li = [int(y) for y in str(x)]
        for i in range(int(len(li)/2)):
            if li[i] != li[-i-1]:
                return False
        return True