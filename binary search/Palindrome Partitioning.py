class Solution:
    def partition(self, s: str):
        ans=[]
        def backtrack(temp,i):
            if i==len(s):
                ans.append(temp.copy())
                return
            temp.append(s[i])
            backtrack(temp.copy(),i+1)
            temp.pop()
            if temp and temp[-1]+s[i]==(temp[-1]+s[i])[::-1]:
                temp[-1]+=s[i]
                backtrack(temp.copy(),i+1)
        backtrack([],0)
        return ans


x=Solution()
print(x.partition("aab"))