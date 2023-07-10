class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        cLen=len(matrix[0])-1 # number of columns
        while(l<=r):
            mid=l+((r-l)//2)
            
            if matrix[mid][0]<=target and matrix[mid][cLen]>=target:
                l,r=0,cLen
                while l<=r:
                    cmid=(l+r)//2
                    if matrix[mid][cmid]==target:
                        return True
                    elif matrix[mid][cmid]<target:
                        l=cmid+1
                    else:
                        r=cmid-1
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
        return False

x=Solution()
print(x.searchMatrix([[1,3,5]],1))