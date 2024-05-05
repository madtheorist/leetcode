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
    
    @classmethod
    def lengthOfLongestSubstring(cls, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/

        return max length of substring without repeating characters
        "abcabcbb" -> 3
        "pwwkew" -> 3
        "abcabcd" -> 4
        "dvdf" -> 3
        """
        # not so great - need to leverage sets (see neetcode)
        if not s:
            return 0
        max_length = 0
        left, right = 0, 0
        while right < len(s) - 1:
            cur = s[left:right+1]
            if s[right+1] in cur:
                max_length = max(max_length, right - left + 1)
                left += 1
            else:
                right += 1
        if s[-1] not in s[left:-1]:
            max_length = max(max_length, right - left + 1)
        return max_length
