import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=r=0
        q=collections.deque()
        output=[]
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]: # appending the highest value in our queue
                q.pop()
            q.append(r)
            
            if l>q[0]: # poping out of bound value
                q.popleft()
                
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
            
            
            
        
        