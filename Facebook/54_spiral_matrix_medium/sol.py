class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recursion(matrix, ret):
            # Single row
            if len(matrix) == 1:
                ret += matrix[0]
                return
            # Single col
            elif len(matrix[0]) == 1:
                for row in matrix:
                    ret += row
                return
            # two rows
            elif len(matrix) == 2:
                ret += matrix[0]
                matrix[-1].reverse()
                ret += matrix[1]

            # General case and two col case
            # General case requires popping + recursion, two cols will return
            else:
                # Top
                ret += matrix[0]
                # Mid left and right
                temp = []
                for i in range(1, len(matrix) - 1):
                    temp.append(matrix[i][0])
                    ret.append(matrix[i][-1])
                    matrix[i].pop()
                    matrix[i].pop(0)
                # Bottom
                matrix[-1].reverse()
                ret += matrix[-1]
                # Mid-left
                temp.reverse()
                ret += temp

                # Two columns
                if len(matrix[0]) == 2:
                    return
                # General
                else:
                    matrix.pop(0)
                    matrix.pop(-1)
                    recursion(matrix, ret)

        if not matrix: 
            return []
        ret = []
        recursion(matrix, ret)
        return ret
