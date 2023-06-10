#Bruteforce
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         tot_product=1
#         length=len(nums)
#         zero=None
#         for i in nums:
#             if i==0 and not zero:
#                 zero=tot_product
#             elif zero:
#                 zero=zero*i
#             tot_product=i*tot_product
            
#         result =[None]*length
        
#         for i in range(0,length,1):
#             if nums[i]==0:
#                 result[i]=zero
#             else:
#                 result[i]=int(tot_product/nums[i])
#         return result             
  

# optimal answer
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:  
        length=len(nums)
        pre=1 # this is prefix 
        pos=1 # this is postfix
        # [1,2,3,4] here for 2 prefix is 1 and post fix is 3*4 i.e 12. therefore the result is 12*1=12
        
        res=[1]*len(nums)
        for i in range(len(nums)):
            
            res[i]*=pre # for prefix
            pre*=nums[i]
            
            res[length-1-i]*=pos # for postfix
            pos*=nums[length-1-i]
        
        return res
             
            
            
            
            
            
        
x = Solution()
print(x.productExceptSelf([-1,1,0,-3,3]))

