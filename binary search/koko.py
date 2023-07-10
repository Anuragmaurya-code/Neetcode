# import math
# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         # Brute force
#         k=1
#         sum=0
#         while (k and sum!=h):
#             sum=0
#             for pile in piles:
#                 sum=sum+math.ceil(pile/k)
#                 if sum > h:
#                     k=k+1
#                     break
#         return k
 
# optimized
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        
        while (l<=r):
            hours=0
            k=(l+r)//2
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours<=h: # may be answer hours are less means k has grown bigger
                res=min(res,k)   
                r=k-1    
            else: # perfect k
                l=k+1
                
        return res

x=Solution()
print(x.minEatingSpeed([3,6,7,11],8))