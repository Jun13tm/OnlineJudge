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
            # if no opened parenthesis
            if not stack or dic[item] != stack[-1]:
                stack.append(item)
            # if match the most resent opened parenthesis
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False