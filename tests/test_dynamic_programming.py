import pytest
from solutions.dynamic_programming import DP

def test_climb_stairs():
    assert DP.climbStairs(1) == 1
    assert DP.climbStairs(2) == 2
    for n in range(3, 46):
        assert DP.climbStairs(n) == (DP.climbStairs(n-1) + DP.climbStairs(n-2))

@pytest.mark.parametrize("cost, output", [
    ([20, 10], 10),
    ([10, 20], 10),
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([0, 0, 1, 0], 0),
    ([0,0,1,1], 1)
    ])
def test_min_cost_climbing_stairs(cost, output):
    assert DP.minCostClimbingStairs(cost) == output