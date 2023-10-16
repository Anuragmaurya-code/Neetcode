class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        maxF=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0) # updating the count
            maxF=max(maxF,count[s[r]])
            while ((r-l+1)-maxF)>k:# checking valid substring i.e window length - max number of char
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        


x=Solution()
print(x.characterReplacement("AABABBA",1))