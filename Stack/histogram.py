class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[] # pair of start index and height
        maxArea=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h: # area cannot be extended further
                ind,hei=stack.pop()
                start=ind
                area=(i-ind)*hei # (end width - start width)*height
                maxArea=max(maxArea,area)
            stack.append([start,h])
            
        while stack: # elements in stack till end
            ind,hei=stack.pop()
            length=len(heights)
            area=h*(length-i)
            maxArea=max(maxArea,h*(len(heights)-i)) # for example 6 - 0 = 6 so it started from 0 index till 6th index
        return maxArea  
x=Solution()
print(x.largestRectangleArea([1,1]))
        