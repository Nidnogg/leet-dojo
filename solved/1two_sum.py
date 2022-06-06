from __future__ import annotations

# Brute Force approach
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashM = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if(complement in hashM):
                return [idx, hashM[complement]]
            else:
                hashM[nums[idx]] = idx
        

sl = Solution()

print(sl.twoSum([3,2,4], 6))


        
        