class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = [item for item in s]
        li.reverse()
        count = 0
        flag = -1
        for item in li:
            if flag == -1:
                if item == ' ':
                    continue
                else:
                    flag = 1
            if item == ' ':
                break
            else:
                count += 1
        return count