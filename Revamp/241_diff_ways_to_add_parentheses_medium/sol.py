import operator

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul}        
        
        def recursion(string):
            ret_li = []
            for i in range(len(string)):
                if string[i] in operators:
                    l_li = recursion(string[0:i])
                    r_li = recursion(string[i + 1:len(string)])
                    # put back
                    for l_item in l_li:
                        for r_item in r_li:
                            ret_li.append(operators[string[i]](l_item, r_item))
            if not ret_li:
                return [int(string)]
            return ret_li
        
        return recursion(input)             