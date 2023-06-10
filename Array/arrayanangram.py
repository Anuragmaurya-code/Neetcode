
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list) # creates a list with values expected to be list
        print(ans)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            ans[tuple(count)].append(s) # list cannot be keys therefore tuple is taken as they are immutable
                                        # and in  dictionary keys should be hashable and they should be immutable
                                        # (cannot be changed)   
                                        # also append is done as key is list
            print(count)    
        return ans.values()

new=Solution()
ans=new.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
for item in ans:
    print(item)
            
                
                
                    
                
                
                
                
                    
                    
                