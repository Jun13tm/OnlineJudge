class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {}
        dic['I'] = 1
        dic['V'] = 5
        dic['X'] = 10
        dic['L'] = 50
        dic['C'] = 100
        dic['D'] = 500
        dic['M'] = 1000

        li = list(s)
        su = 0
        prev_val = 0
        for i in range(len(li)):
            if dic[li[i]] > prev_val:
                su -= 2*prev_val
            su += dic[li[i]]
            prev_val = dic[li[i]]
        return su