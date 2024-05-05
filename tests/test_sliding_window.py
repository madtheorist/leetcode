import pytest
from src import SlidingWindow


@pytest.mark.parametrize(
    "prices, profit",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_max_profit(prices, profit):
    assert SlidingWindow.maxProfit(prices) == profit