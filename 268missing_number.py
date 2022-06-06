# Terrible runtime - try fix
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            try:
                nums.index(i)
            except ValueError:
                return i