class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        mx = 0

        while right < len(prices):
            
            number = prices[right] - prices[left]

            if number > 0:
                mx = max(number, mx)
                right += 1
            else:
                left = right
                right += 1
        
        return mx