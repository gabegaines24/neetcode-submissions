class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        idea, use sorted strings as key, if key == word.sorted(), then it is 
        in a group
        """
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())