def fib_memoization(n,dp): # memoization
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fib_memoization(n-1,dp)+fib_memoization(n-2,dp)
    return dp[n]

def fib_tabulation(n,dp): # tabulation
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def fib_tabulation_better_space(n): # tabulation
    prev=1
    prev2=0
    for i in range(2,n+1):
        temp=prev+prev2
        prev2=prev
        prev=temp
    return prev

 
if __name__=='__main__':
    n=5
    dp=[-1]*(n+1)
    print(fib_tabulation_better_space(n))