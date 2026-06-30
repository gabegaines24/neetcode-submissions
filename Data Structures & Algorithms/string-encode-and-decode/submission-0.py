class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
    
        while i < len(s):           # Outer loop - 4 spaces
            j = i                    # 8 spaces (inside outer while)
            while j < len(s) and s[j] != '#':  # 8 spaces (same level as j = i)
                j += 1               # 12 spaces (inside inner while)
            length = int(s[i:j])     # 8 spaces (back to outer while level)
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
    
        return res   

