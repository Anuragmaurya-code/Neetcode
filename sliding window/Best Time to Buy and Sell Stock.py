class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy,sell,profit=prices[0],0,0
        
        for i in range(1,len(prices)):
            if prices[i]-buy>profit:
                sell=prices[i]
                profit=sell-buy
            if prices[i]<buy:
                buy=prices[i]

        return profit

x=Solution()
print(x.maxProfit([2,1,2,1,0,1,2]))