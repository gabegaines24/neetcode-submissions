class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = {0: 1} #prefix: seen #
        for x in nums:
            prefix_sum += x
            #if (prefix-k has been found, there exists a sub array to k)
            count += seen.get(prefix_sum-k,0)
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
        return count