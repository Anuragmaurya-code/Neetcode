class Solution:
    def combinationSum2(self, candidates, target: int) :
        candidates.sort()
        ans=[]
        def backtrack(sum,ind,nums):
            if sum==target:
                ans.append(nums.copy())
                return
            if sum>target or ind>=len(candidates):
                return 
            nums.append(candidates[ind])
            backtrack(sum+candidates[ind],ind+1,nums)
            while ind+1<len(candidates) and candidates[ind]==candidates[ind+1]:
                ind+=1
            nums.pop()
            backtrack(sum,ind+1,nums)
        backtrack(0,0,[])
        return ans

        
    
x=Solution()
print(x.combinationSum2([10,1,2,7,6,1,5],8))
