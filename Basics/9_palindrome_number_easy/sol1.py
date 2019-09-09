class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            li = [str(y) for y in str(x)]
            mid_idx = int(len(li)/2)
            # Odd length integer
            if len(li) % 2 == 1:
                li.pop(mid_idx)
        front = li[:mid_idx]
        end = li[mid_idx:]
        front.reverse()
        for i in range(len(front)):
            if front[i] != end[i]:
                return False
        return True    