# class Solution:
#Takes extra space
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         ans=0
#         maxLeft,maxRight,L=[None]*len(height),[None]*len(height),[None]*len(height)
#         size=len(height)-1
#         maxL,maxR=0,0
#         for i in range(len(height)):
#             maxLeft[i]=maxL
#             maxRight[size-i]=maxR
#             maxL=max(maxL,height[i])
#             maxR=max(maxR,height[size-i])
#         for i in range(len(height)):
#             L[i]=min(maxLeft[i],maxRight[i])
#             temp=min(maxLeft[i],maxRight[i])-height[i]
#             if(temp>0):
#                 ans+=temp
#         return ans
    
# optimal with no extra space consumption
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        res,l,r=0,0,len(height)-1
        maxL,maxR=height[l],height[r]
        while(l<r):
            if maxL<maxR:
                l+=1
                maxL=max(height[l],maxL)
                res+=maxL-height[l]
                
            else:
                r-=1
                maxR=max(height[r],maxR)
                res+=maxR-height[r]
            # end ka maxL and maxR same honga aur unpa koi bhi water nhi store hoga   
        return res
x=Solution()
print(x.trap([0,1,0,2,1,0,1,3,2,1,2,1]))