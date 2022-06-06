from __future__ import annotations

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = dict.fromkeys(nums, "key")
        if(len(hashMap) !=  len(nums)):
            return True
        else:
            return False
        
        

sl = Solution()

print(sl.containsDuplicate([1,2,1,2]))
print(sl.containsDuplicate([1,2,3,4]))


        
        