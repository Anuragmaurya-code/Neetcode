class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydist=set([])
        for item in nums:
            if item in mydist:
                return True
            else :   
                mydist.add(item)
        return False