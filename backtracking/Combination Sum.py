class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def dfs(k,sum,visit):
            if sum==target:
                ans.append(visit)
                return
            if k>=len(candidates) or sum>target:
                return
            dfs(k,sum+candidates[k],visit+[candidates[k]]) # adding current index to list
            dfs(k+1,sum,visit) # just do nothing
            
        dfs(0,0,[])
        return ans
x=Solution()
print(x.combinationSum([2,3,6,7],7))

