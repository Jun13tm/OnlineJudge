'''
• Complexity:
    ○ O(n^2)
• Topics:
    ○ dp
确定在任意一个index i是否能成功Break，取决于前面所有index j是否能成功break and s[j,i]是否为一个valid word。
注意dp array前面加一个True padding for convenience purpose
Followup:
     If True, return the fewest number of words that make up this string
遇到True时不break，而是loop完所有的j index，记录最少的单词数。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # requires a padding for convenience
        dp = [False] * (len(s) + 1)
        dp[0] = True
        set_ = set()
        for word in wordDict:
            set_.add(word)
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in set_:
                    dp[i] = True
                    break
        return dp[-1]

    # Followup: Return -1 if false, otherwise return fewest # of words
    def wordBreak(self, s: str, wordDict: List[str]) -> int:
        dp = [-1] * (len(s) + 1)
        dp[0] = 0
        set_ = set()
        for word in wordDict:
            set_.add(word)
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] >= 0 and s[j:i] in set_:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]