class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea: number: freq, then sort descending and return n from typed list
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        sorted_keys = sorted(d.keys(), key=lambda n: d[n], reverse=True)
        return sorted_keys[:k]
