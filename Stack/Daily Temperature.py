class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[] # pair of value and stack
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackI=stack.pop()
                res[stackI]=(i-stackI)
            stack.append([t,i])
        return res

        

        

x=Solution()
print(x.dailyTemperatures([73,74,75,71,69,72,76,73]))