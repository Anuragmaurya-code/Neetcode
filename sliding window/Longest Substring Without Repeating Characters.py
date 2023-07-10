class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store={}
        l,r,res=0,0,0
        while r<len(s):
            if s[r] in store : #abca as a apeared
                l=store[s[r]]+1 #bca considering this window
                r=store[s[r]]+1
                store={}
            temp=r-l+1
            res=max(temp,res)
            store[s[r]]=r
            r+=1
        return res

x=Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))