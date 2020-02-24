class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        li = [(-1,0)] * n
        prev = -1

        for i in range(len(logs)):
            id_, op, time = logs[i].split()
            
            # hang previous log
            if prev != -1:
                duration = time - logs[prev][1]
                if op == "end": duration += 1
                li[prev] = (-1, li[prev][1] + duration) 

            if op == "start":
                li[id_] = (time, li[id_][1])
                prev = id_
            else:
                prev = -1
            
        return [li[i][1] for i in range(n)]