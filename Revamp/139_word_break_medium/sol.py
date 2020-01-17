class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        dic = {item : 1 for item in wordDict}
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in dic for j in range(i)),
        return ok[-1]