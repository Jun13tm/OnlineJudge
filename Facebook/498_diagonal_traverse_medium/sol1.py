class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix) # num Rows
        n = len(matrix[0]) # num Cols
        dic = {}
        ret = []

        for i in range(m):
            for j in range(n):
                su = i + j
                if su not in dic:
                    dic[su] = [(i, j)]
                else:
                    dic[su].append((i, j))
        for key in dic:
            dic[key].sort(key=lambda x: x[1])
            if key % 2 == 1:
                dic[key].reverse()
        for key in range(len(dic)):
            for item in dic[key]:
                ret.append(matrix[item[0]][item[1]])
        return ret