class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) % 2 == 1:
            return False
        dic = {}
        dic['('] = ')'
        dic[')'] = '('
        dic['{'] = '}'
        dic['}'] = '{'
        dic['['] = ']'
        dic[']'] = '['
        stack = []
        for item in list(s):
            if len(stack) == 0:
                stack.append(item)
                continue
            if dic[item] == stack[-1]:
                stack.pop()
                continue
            stack.append(item)
        if len(stack) == 0:
            return True
        else:
            return False