class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # without extra memory nor space only two pointer(slow and fast is a valid options)
        s,f=0,0
        while True:
            s+=1
            f+=2
            if f>len(nums)-1:
                f=f-len(nums)-1
            if s>len(nums)-1:
                s=s-len(nums)
            if nums[s]==nums[f] and s!=f:
                return nums[s]
        return -1

x=Solution()
print(x.findDuplicate([3,1,3,4,2]))