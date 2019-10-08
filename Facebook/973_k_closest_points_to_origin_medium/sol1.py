class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points: return []
        
        # Naive
        li, ret = [], []
        for i in range(len(points)):
            su = points[i][0]**2 + points[i][1]**2
            li.append((su, i))
        li.sort()
        for i in range(K):
            ret.append(points[li[i][1]])
        return ret