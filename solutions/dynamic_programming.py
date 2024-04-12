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