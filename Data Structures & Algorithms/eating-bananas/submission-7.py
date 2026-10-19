class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hrs = sum(math.ceil(p / k) for p in piles)

            if hrs <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res