'''
    • Complexity:
        ○ O(m*n)
    • Topics
        ○ dfs/bfs
用DFS找出所有disjoint sets的问题，count call了多少次explore。如果一个cell被explore, 当做
water来看待（val = 0)。注意"delta"的用法，可以用少量代码加上上下左右4个neighbors
注意在加入neighbor的时候就应该mark为visited，不然可能重复添加coordiates进stack/queue。在
BFS测试的时候出现了TLE error。
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(grid, row, col):
            stack = [(row, col)]
            grid[row][col] = "0"
            while stack:
                i, j = stack.pop(0)
                # Add all neighbors
                deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for x, y in deltas:
                    i_, j_ = i + x, j + y
                    # Make sure neighbor coordinate is in bound
                    if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[0]):
                        if grid[i_][j_] == "1":
                            # 注意在add neighbor的时候就mark这个coordinate为visited
                            grid[i_][j_] = "0"
                            stack.append((i_, j_))
            
        # No edge case to handle
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    explore(grid, i, j)
                    count += 1
        return count