class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea: number: freq, then sort descending and return n from typed list
        bucket = [[] for _ in range(len(nums) +1)]
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, freq in count.items():
            bucket[freq].append(n)
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
