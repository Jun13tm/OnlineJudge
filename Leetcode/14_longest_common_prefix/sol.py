class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        
        # Find the shortest string
        s_len = len(strs[0])
        for string in strs:
            if len(string) < s_len:
                s_len = len(string)
        
        ret = ''
        for i in range(s_len):
            curr = strs[0][i]
            for row in strs:
                if row[i] != curr:
                    return ret
            ret += curr
        return return