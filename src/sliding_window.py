from typing import List

class SlidingWindow:

    @classmethod
    def maxProfit(cls, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        [7,1,5,3,6,4]
        [7,6,4,3,1]
        """
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            test = prices[right] - prices[left]
            if test > max_profit:
                max_profit = test
            if prices[left] > prices[right]:
                left = right
            right += 1
        return max_profit

