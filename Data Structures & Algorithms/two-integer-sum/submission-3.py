class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            x = target - n
            if x in indices:
                return [indices[x], i]
            indices[n] = i