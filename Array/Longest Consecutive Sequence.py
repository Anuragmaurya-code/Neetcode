# code using hashset 
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         my_hash={}
#         for num in nums:
#             ind=num
#             if ind-1 in my_hash.keys():
#                 my_hash[ind]=my_hash[ind-1]+1
#             else:
#                 my_hash[ind]=1
#             while ind+1 in my_hash.keys():
#                 my_hash[ind+1]=my_hash[ind]+1
#                 ind+=1
#         ans=max(my_hash.values())
#         return ans

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet=set(nums)
        
        longest=0
        
        for n in numSet:
            if (n-1) not in numSet:
                length=0
                while n+length in numSet:
                    length+=1
                longest=max(longest,length)
        return longest
                
            
x=Solution()
print(x.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))