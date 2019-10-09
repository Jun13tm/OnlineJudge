class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j not in dic:
                    dic[i - j] = matrix[i][j]
                else:
                    if matrix[i][j] != dic[i - j]:
                        return False
        return True