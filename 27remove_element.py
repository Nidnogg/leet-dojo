class Solution:
    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high
    
    def quick_sort(self, array, start, end):
        if start >= end:
            return

        p = self.partition(array, start, end)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)
        
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            print(nums[i])
            if(nums[i] == val):
                print('removing')
                nums[i] = 99
                k += 1
            i+=1
        
        self.quick_sort(nums, 0, len(nums) - 1)
  
        return k
        
                
                
        