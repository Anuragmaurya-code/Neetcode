class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newS=""
        for c in s:
            if 97<=ord(c)<=122 or 48<=ord(c)<=57:
                newS+=c
        length=len(newS)
        for i in range(length):
            if newS[i]!=newS[length-1-i]:
                return False
        return True
            

x= Solution()
print(x.isPalindrome("A man, a plan, a canal: Panama"))