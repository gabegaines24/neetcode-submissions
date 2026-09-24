class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {} #char: freq
        dt = {} #char: freq

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            ds[s[i]] = 1 + ds.get(s[i], 0)
            dt[t[i]] = 1 + dt.get(t[i], 0)
        
        return ds == dt