class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # while nums[i] + 1 exists, length += 1, record max length
        numSet, res = set(nums), 0

        for n in nums:
            if n - 1 not in numSet:
                curr = 1
                while n + curr in numSet:
                    curr += 1
                res = max(res, curr)
        
        return res