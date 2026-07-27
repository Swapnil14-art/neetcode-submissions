class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0 
        ans = 0
        for i in range (len(prices)):
            for j in range (i, len(prices)):
                if prices[i] < prices[j]:
                    diff = prices[j] - prices[i]
                if diff > ans :
                    ans = diff
        return ans
        
                    