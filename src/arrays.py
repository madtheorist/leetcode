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
            
    @classmethod
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        https://leetcode.com/problems/group-anagrams/
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        O(m*nlogn)
        """
        counters = {}
        for word in strs:
            test = ''.join(sorted(word))
            counters[test] = [word] + counters.get(test, [])
        return [l for l in counters.values()]
    
    @classmethod
    def topKFrequent(cls, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        # k most frequent elements
        hashmap = {num: freq for num, freq in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)}
        return [num for num in hashmap][:k]