class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minV = float('inf')
        maxV = 0 

        for price in prices:
            minV = min(minV, price)
            maxV = max(maxV, price - minV)

        return maxV