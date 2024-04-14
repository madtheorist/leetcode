import pytest
from src import Arrays

def test_two_sum():
    assert set(Arrays.twoSum([2, 7, 11, 15], 9)) == set([0, 1])
    assert set(Arrays.twoSum([3, 2, 4], 6)) == set([1, 2])
    assert set(Arrays.twoSum([3, 3], 6)) == set([0, 1])

def test_group_anagrams():
    assert Arrays.groupAnagrams([""]) == [[""]]
    assert Arrays.groupAnagrams(["a"]) == [["a"]]