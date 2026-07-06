class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            size = len(s)
            res += (str(size) + "#" + s)

        return res

    def decode(self, s: str) -> List[str]:
        res, l = [], 0

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            
            size = int(s[l:r])
            r += 1
            word = s[r: r + size]
            res.append(word)

            l = r + size

        return res
    