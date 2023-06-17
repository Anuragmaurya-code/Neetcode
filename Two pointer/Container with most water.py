# Bruteforce approach
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         ans=0
#         for i in range(len(height)-1):
#             area=0
#             for j in range(0,len(height)-1):
#                 breadth=j-i
#                 length=min(height[i],height[j])
#                 area=length*breadth
#             ans=max(area,ans)
#         return ans
                
                

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res,l,r=0,0,len(height)-1
        while l<r:
            area=(r-l)*min(height[l], height[r])
            res=max(area,res)
            #condition to change pointer
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

x=Solution()
print(x.maxArea([1,8,6,2,5,4,8,3,7]))