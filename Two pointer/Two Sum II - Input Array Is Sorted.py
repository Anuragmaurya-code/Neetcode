class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        j = len(numbers)-1
        i=0
        while (i<=j):
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            elif sum<target:
                i+=1
            else:
                j-=1
        return []
x=Solution
print(x.twoSum([-1,0],-1))