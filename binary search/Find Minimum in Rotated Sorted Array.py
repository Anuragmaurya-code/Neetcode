class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1
        x=nums[0]
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]<x:
                r=mid-1
            else:
                l=mid+1
        return nums[l]

x=Solution()
print(x.findMin([3,4,5,1,2]))