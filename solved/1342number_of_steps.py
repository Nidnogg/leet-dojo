class Solution:
    # Default strategy, way better memory usage, slower runtime
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while(num != 0):
            if(num % 2 == 0):
                num / 2
                steps += 1
            else:
                num - 1
                steps += 1
        
        return steps
    # Recursive strategy - more memory, but faster runtime
    # def numberOfSteps(self, num: int) -> int:
    #     if num == 0:
    #         return 0
    #     elif num % 2 == 0:
            
    #         return 1 + self.numberOfSteps(num / 2)
    #     else:
            
    #         return 1+ self.numberOfSteps(num - 1)