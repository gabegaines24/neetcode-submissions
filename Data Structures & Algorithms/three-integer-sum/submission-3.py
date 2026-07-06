class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums)):

            if nums[a] == nums[a - 1] and a > 0: 
                continue

            l,r = a + 1, len(nums) - 1
            while l < r:
                Tsum = nums[a] + nums[l] + nums[r]

                if Tsum > 0:
                    r -= 1
                elif Tsum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
        return res            