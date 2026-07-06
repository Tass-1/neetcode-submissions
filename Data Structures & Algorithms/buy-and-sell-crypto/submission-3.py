class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 10000
        maxP = 0
        left = 0
        right = len(prices)-1
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)):
                maxP = max(maxP , prices[j] - prices[i])
        return maxP