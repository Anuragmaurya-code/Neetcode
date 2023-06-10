from collections import defaultdict

# Bruteforce approach 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #bucket sort is used
        
        count={}

        for num in nums:
            count[num]=1+count.get(num, 0)
        
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True)) #here lamda 
        # is anonymous function and item is given index 1, key has index 0 and value has index 1
        # therefore sorting is done based on values 
        
        result = []
        for key, value in count.items():
            result.append(key)
            if len(result)==k:
                return result

# optimal approach
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         #bucket sort is used
        
#         count={}
#         frequency=[[] for i in range(len(nums)+1)] #The line frequency=[[] for i in range(len(nums)+1)] 
#         # creates a list of empty lists, where the length of the outer list is equal to len(nums) + 1.
        
#         for num in nums:
#             count[num]=1+count.get(num, 0)
            
#         for n,c in count.items():
#             frequency[c].append(n)
        
#         result=[]
        
#         for i in range(len(frequency)-1,0,-1):
#             for n in frequency[i]:
#                 result.append(n)
#                 if(len(result)==k):
#                     return result
 

            

                       
        
x=Solution()
print(x.topKFrequent([1,1,1,2,2,3],2))