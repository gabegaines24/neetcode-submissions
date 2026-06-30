class Solution:
    def isValid(self, s: str) -> bool:
        ClosedToOpen = {"}": "{", "]": "[", ")": "("}
        word = []

        for c in s:
            if c in ClosedToOpen:
                if word and word[-1] == ClosedToOpen[c]:
                    word.pop()
                else:
                    return False
            else:
                word.append(c)
        
        return True if not word else False