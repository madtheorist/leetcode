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

@pytest.mark.parametrize(
    "string, length",
    [
        ("abcabcbb", 3),
        ("bbbb", 1),
        ("pwwkew", 3),
        ("abcabcd", 4),
        ("dvdf", 3)
    ],
)
def test_length_of_longest_substring(string, length):
    assert SlidingWindow.lengthOfLongestSubstring(string) == length