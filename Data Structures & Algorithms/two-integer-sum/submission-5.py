class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {} #number: index

        for i, n in enumerate(nums):
            comp = target - n
            if comp in hashM:
                return(sorted([i, hashM[comp]]))
            hashM[n] = i