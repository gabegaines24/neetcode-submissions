from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter automatically builds the frequency dictionaries and handles the comparison
        return Counter(s) == Counter(t)
