class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        desc = sorted(freq.items(),key = lambda y: y[1], reverse=True)

        res = [k for k,v in desc]
        return res[:k]
        