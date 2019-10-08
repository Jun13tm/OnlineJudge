class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # Mono inc/dec, equal acceptable for both
        if len(A) <= 2: return True
        status = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                continue
            elif A[i] > A[i-1]:
                if status == 0:
                    status = 1
                    continue
                if status == -1:
                    return False
            else:
                if status == 0:
                    status = -1
                    continue
                if status == 1:
                    return False
        return True