# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack=[]
#         for i in range(len(s)):
#             if(s[i] in ['(','{','[']):
#                 stack.append(s[i])
#             elif(len(stack)>0):
#                 if(s[i]==')' and stack[-1]=='(' or s[i]==']' and stack[-1]=='[' or s[i]=='}' and stack[-1]=='{'):
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 return False
#         if(len(stack)==0):
#             return True
#         return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            

x=Solution()
print(x.isValid("]"))