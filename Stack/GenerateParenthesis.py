class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack=[]
        result=[]
        
        def backtrack(openN, closeN):
            if openN==closeN==n:
                result.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1, closeN)
            if closeN<n:
                stack.append(")")
                backtrack(openN,closeN+1)
        return result
                
        