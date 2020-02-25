'''
752: Open the Lock Medium 
    • Complexity: 
        ○ O(1) - fixed number of possible moves
    • Topics: 
        ○ bfs
比较naive的bfs，可能有更好的Optimization方法。比方说target = 5XXX，但2XXX是一个deadend，
那么的一个0只能向下拨动。
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends or "0000" in deadends:
            return -1
        
        de = set()
        for deadend in deadends:
            de.add(deadend)
        
        moves = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1], [0, 0, 0, -1]]
        queue = [("0000", 0)]
        
        while queue:
            curr, pathlen = queue.pop(0)
            curr = [int(l) for l in curr]
            # Add all 8 possible moves
            for move in moves:
                combination = [str((move[i] + curr[i]) % 10) for i in range(len(move))]
                combination = "".join(combination)
                if combination == target:
                    return pathlen + 1
                if combination not in de:
                    # Treat visited nodes as deadends
                    de.add(combination)
                    queue.append((combination, pathlen + 1))
        return -1