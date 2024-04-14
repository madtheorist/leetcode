from typing import List

class Arrays:

    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/
        nums = [2, 7, 11, 15], target = 9, output = [0, 1]
        """
        num_2_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            # check if diff exists in num_2_index dict
            if diff not in num_2_index:
                num_2_index[num] = i
            else:
                return [i, num_2_index[diff]]
        
        

