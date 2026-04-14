from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # If set has fewer elements than the list, there are duplicates
        return len(nums) != len(set(nums))
