'''
• Complexity: 
    ○ O(n); O(n)
• Topics: 
    ○ sliding_window
• Related:
    ○ LC1100 (subsarray with size k)
    ○ LC340
把问题简化到最多k个different integers。然后reduction(k) - reduction(k-1)得出结果。
Sliding window每次只检查当前window下，所有以end pointer结尾的subarray是否valid。
比方说[1,2,1,2]这个window，[1,2,1,2],[2,1,2],[1,2],[2]为valid。
Cornor case: k = 0 - return 0, also如果不允许重复，在return前用hashmap处理。
'''
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def reduction(k):
            i = 0
            dic = {}
            su = 0
            
            for j in range(len(A)):
                # Update dictionary
                if A[j] not in dic or dic[A[j]] == 0:
                    k -= 1
                    dic[A[j]] = 1
                else:
                    dic[A[j]] += 1
                
                # If k falls below 0
                while k < 0:
                    dic[A[i]] -= 1
                    if dic[A[i]] == 0:
                        k += 1
                    i += 1
                    
                # Update sum
                su += j - i + 1
            return su
        return reduction(K) - reduction(K - 1)