'''
• Complexity: 
    ○ O(m + n); O(min(m, n))
• Topics: 
    ○ array
    ○ hash
将其中一个array的所有element load进hashmap，value : count，再loop第二个array。如果value存在于hashmap里，decrement count，并且把这个element加入intersection array。认为hash的操作都是constant time，time complexity为O(m + n)。space为m和n中较小的那个，hashmap的长度为O(min(m,n))
Followup: 如果两个array都太大，无法一次性录入memory?
    - hash用来记录array1 counts的时候，分段load
array2也分段load
'''
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        intersection = []
        dic = defaultdict(int)
        for item in nums1:
            dic[item] += 1
        for item in nums2:
            if dic[item] > 0:
                intersection.append(item)
                dic[item] -= 1
        return intersection