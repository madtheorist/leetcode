from solutions.dynamic_programming import DP

def test_climb_stairs():
    assert DP.climbStairs(1) == 1
    assert DP.climbStairs(2) == 2
    for n in range(3, 46):
        assert DP.climbStairs(n) == (DP.climbStairs(n-1) + DP.climbStairs(n-2))