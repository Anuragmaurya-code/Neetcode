class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # searching pivot
        l,r=0,len(nums)-1
        x=0
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]<nums[x]:
                x=mid
                r=mid-1
            else:
                l=mid+1
        l,r=x-len(nums),x-1

        while(l<=r):
           mid=(l+r)//2
           if nums[mid]==target:
               if mid<0:
                   mid=mid+len(nums)
               return mid
           elif nums[mid]<target:
                l=mid+1
           else:
                r=mid-1
        return -1
        
            
x=Solution()
print(x.search([4,5,6,7,0,1,2],0))