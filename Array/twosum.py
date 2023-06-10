
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic={}
        for i,n in enumerate(nums): #i for index and n for value
            if n in mydic:
                return [mydic[n],i]
            else:
                mydic[target-n]=i
            
                
                
                
                