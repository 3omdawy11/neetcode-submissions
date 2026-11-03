class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        left = 0
        right = 1

        mx = 0

        while left < right and right < len(prices):
            if prices[right] > prices[left]:
                mx = max(prices[right] - prices[left], mx)
                right += 1
            else:
                left = right
                right += 1

        return mx