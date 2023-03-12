# Problems with this Solution - can't delete in place without overwriting the next indexes. look into enumerate and frozenset
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerosOnly = True
        for num in nums:
            if num != 0:
                zerosOnly = False
                break
        if not zerosOnly:
            toDelete = []
            startingLen = len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums.append(nums[i])
            print('inside deletion loop')
            print(nums)
            for i in range(startingLen):
                print(nums[i])
                if nums[i] == 0:
                    toDelete.append(i)

            print('toDelete', toDelete)
            for index in toDelete:

                print('poopping', index)
                nums.pop(index)
