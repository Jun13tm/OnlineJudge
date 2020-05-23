class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def helper(temp, digits):
            if len(digits) == 0:
                output.append(temp)
            else:
                for l in dic[digits[0]]:
                    helper(temp + l, digits[1:])
            
        output = []
        if digits:
            helper("", digits)
        return output