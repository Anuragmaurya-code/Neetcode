class Solution:
    def solveNQueens(self, n: int):
        ans=[]
        def backtrack(i,temp):
            if i==n:
                ans.append(temp.copy())
                return
            found=True
            for x in range(0,n):
                for y in range(len(temp)):
                    if i==y or x==temp[y] or (i-x)==(y-temp[y]) or (i+x)==(y+temp[y]):
                        found=False
                        break
                    else:
                        found=True
                if found:
                    temp.append(x)
                    backtrack(i+1,temp)
                    temp.pop()
        
        backtrack(0,[])
        newAns=[]
        for a in range(len(ans)):
            sub=[]
            for x in range(len(ans[a])):
                t=""
                for y in range(n):
                    if y==ans[a][x]:
                        t+="Q"
                    else:
                        t+="."
                sub.append(t)
            newAns.append(sub)
        return newAns

x=Solution()
print(x.solveNQueens(4))