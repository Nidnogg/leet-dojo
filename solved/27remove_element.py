from __future__ import annotations

# Quicksort solution (terrible runtime, terrible memory usage)
# class Solution:
#     def partition(self, array, start, end):
#         pivot = array[start]
#         low = start + 1
#         high = end

#         while True:
     
#             while low <= high and array[high] >= pivot:
#                 high = high - 1

#             # Opposite process of the one above
#             while low <= high and array[low] <= pivot:
#                 low = low + 1

#             if low <= high:
#                 array[low], array[high] = array[high], array[low]
#             else:
#                 break

#         array[start], array[high] = array[high], array[start]

#         return high
    
#     def quick_sort(self, array, start, end):
#         if start >= end:
#             return

#         p = self.partition(array, start, end)
#         self.quick_sort(array, start, p-1)
#         self.quick_sort(array, p+1, end)
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         i = 0
#         while i < len(nums):
#             if(nums[i] == val):
#                 k += 1
#                 nums[i] = 99
#             i+=1
#         self.quick_sort(nums, 0, len(nums) - 1)
#         k = len(nums) - k
#         return k

# Python sort() solution, faster than 90%
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if(nums[i] == val):
                k += 1
                nums[i] = 99
            i+=1
        nums.sort()
        k = len(nums) - k
        return k         
sl = Solution()
sl.removeElement([0,1,2,2,3,0,4,2], 2)

                
                
        