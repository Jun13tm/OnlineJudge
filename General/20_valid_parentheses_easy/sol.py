class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def helper(strs):
            if strs == []:
                return ""
            ret = strs[0][:1]
            for i in range(len(strs)):
                # End case
                if strs[i][:1] != ret or strs[i] == "":
                    return ""
                strs[i] = strs[i][1:]
            return ret + helper(strs) 
        
        return helper(strs)