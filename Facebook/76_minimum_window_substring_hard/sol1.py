class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case handling
        if not s or not t: return ""
        if len(t) > len(s): return ""
        if len(s) == 1:
            return "" if s != t else s

        # Sliding window w/o optimization
        left, right = -1, -1
        curr = ()
        count = len(t)

        dic = {}
        for i in range(len(t)):
            dic[t[i]] = -1
        # Loop s
        for i in range(len(s)):
            # update right
            right = i
            # if a valid letter
            if s[right] in dic:
                # if this letter is one missing letter
                if dic[s[right]] == -1:
                    count -= 1
                # update dic
                dic[s[right]] = right

            # check if window is valid
            while count == 0:
                # update minimum size if necessary
                if not curr or right - left < curr[1] - curr[0]:
                    curr = (left, right)

                # Move left
                # if popped letter is required for valid window, count += 1
                if s[left] in dic and dic[s[left]] == left:
                    count += 1
                    dic[s[left]] = -1
                left += 1
        if not curr or curr[0] == -1:
            return ""
        else:
            return s[curr[0]:curr[1]+1]