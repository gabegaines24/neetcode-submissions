class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #idea --> use the sorted string as the key, and enter strings into the List
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)

        return list(res.values())