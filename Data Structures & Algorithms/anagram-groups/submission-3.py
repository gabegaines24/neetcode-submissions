class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #idea --> I want to use the sorted as the key, and put the values into a list
        ana = defaultdict(list)

        for s in strs:
            sSort = sorted(s)
            ana[tuple(sSort)].append(s)
        
        return [v for k,v in ana.items()]