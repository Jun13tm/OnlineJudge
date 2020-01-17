class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Empty list
        if not text1 or not text2:
            return 0
        # 2D, pad first row and first column with 0s 
        li = [[0] for i in range(len(text1)+1)]
        for i in range(len(text2)):
            li[0].append(0)

        # Table Filling
        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                # Case1: same letter
                if text1[row-1] == text2[col-1]:
                    li[row].append(li[row-1][col-1]+1)
                else:
                    li[row].append(max(li[row-1][col], li[row][col-1]))
        print(li)
        return li[-1][-1]