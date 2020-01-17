class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case:
        if not s or not t: return ""
        if len(t) > len(s): return ""
        
        # load letters in t into a dictionary
        dic = {}
        for i in range(len(t)):
            if t[i] in dic:
                dic[t[i]] += 1
            else:
                dic[t[i]] = 1
        
        # Sliding window
        left, right = -1, -1
        curr = ()
        count = len(t)
        
        for right in range(len(s)):
            # if a valid letter
            if s[right] in dic:
                dic[s[right]] -= 1
                # if fulfilled required # of elements
                # count -= 1 at the first time it reaches 0
                if dic[s[right]] >= 0:
                    count -= 1
            # check if a valid window
            while count == 0:
                if left == -1:
                    left = 0
                    continue
                # update min size if necessary
                if not curr or right - left < curr[1] - curr[0]:
                    curr = (left, right)               
                # move left pointer
                # if popped letter is in dictionary
                if s[left] in dic:
                    dic[s[left]] += 1
                    if dic[s[left]] > 0:
                        count += 1
                left += 1

        if not curr or curr[0] == -1:
            return ""
        else:
            return s[curr[0]:curr[1]+1]