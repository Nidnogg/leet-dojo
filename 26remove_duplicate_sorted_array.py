class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        if(len(nums) == 1):
            print(nums)
            return k
        else:
            for i in range(len(nums)):                
                if(i < (len(nums) - 1)):
                    if(nums[i] == nums[i+1]):
                        if(nums[i] == 3): 
                            nums.pop(nums[i])
                        print("popping")
                        nums.pop(nums[i+1])
        k = len(nums)
        return k
            
        