class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursive 
        def helper(text1, text2):
            nonlocal mems
            # Stop condition
            if not text1 or not text2:
                return 0
            if (text1, text2) in mems:
                return mems[(text1, text2)]

            if text1[-1] == text2[-1]:
                ret = 1 + helper(text1[:-1], text2[:-1])
            else:
                ret = max(helper(text1[:-1], text2), helper(text1, text2[:-1]))
            mems[(text1, text2)] = ret
            return ret

        mems = {} # Records tuples
        return helper(text1, text2)