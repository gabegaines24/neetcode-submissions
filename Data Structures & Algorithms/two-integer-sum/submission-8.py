class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use the compliment
        d = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in d:
                return [d[comp], i]
            d[n] = i
        