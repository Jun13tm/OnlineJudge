'''
    • Complexity:
        ○ O(n); O(n) - can be reduced to O(k) or O(1) (use array instead of hashmap)
    • Topics:
        ○ sliding_window
    • Related: 
        ○ LC992 (size of subarray not specified)
算法简单，逐步推进就好了。可以对比一下992，都track有多少个distinct chars正在被使用。
'''
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        # Edge case handling
        if len(S) < K: return 0
        
        dic = {}
        rest = K
        ret = []
        
        for i in range(len(S)):
            if S[i] not in dic or dic[S[i]] == 0:
                dic[S[i]] = 1
                rest -= 1
            else:
                dic[S[i]] += 1
            if i >= K - 1:
                front = i - K + 1
                if rest == 0:
                    ret.append(S[front:i + 1])
                # Before move on
                dic[S[front]] -= 1
                if dic[S[front]] == 0:
                    rest += 1
        return len(ret)