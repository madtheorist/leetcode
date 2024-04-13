from typing import List
from collections import deque

class DP:

    @classmethod
    def climbStairs(cls, n: int) -> int:
        """
        https://leetcode.com/problems/climbing-stairs/
        Fibonacci sequence O(n)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        mylist = [None] * n
        mylist[0], mylist[1] = 1, 2
        for i in range(2, n):
            mylist[i] = mylist[i-1] + mylist[i-2]
        return mylist[-1]
    
    @classmethod
    def minCostClimbingStairs(cls, cost: List[int]) -> int:
        """
        https://leetcode.com/problems/min-cost-climbing-stairs/description/
        O(n) solution
        """
        # cost_cache[i] is min cost to climb to the top starting from ith staircase
        cost_cache = deque(cost[-2:])
        for c in cost[::-1][2:]:
            min_cost = c + min(cost_cache[0], cost_cache[1])
            cost_cache.appendleft(min_cost)
        return min(cost_cache[0], cost_cache[1])

    @classmethod
    def rob(cls, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/house-robber/description/
        Logic:
        - go in order
        - if you rob a given house, then you must skip the next one
        Starting chains:
        - R - 
        - n - R - 
        then skip either two houses or skip one.
        """
        # money_cache[i] is max money gained dfrom to robbing ith house and any houses before
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        money_cache = [nums[0], nums[1], nums[0] + nums[2]]
        for num in nums[3:]:
            max_money = num + max(money_cache[-2], money_cache[-3])
            money_cache.append(max_money)
        return max(money_cache[-1], money_cache[-2])

    

    

        
        
        