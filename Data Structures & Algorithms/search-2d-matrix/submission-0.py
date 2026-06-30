class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            for c in row:
                nums.append(c)

        nums.sort()

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False