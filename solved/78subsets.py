class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtracking(results, path, depth, options):
            if(depth == 0):
                results.append(path[:])
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()
        for i in range(len(nums) + 1):
            backtracking(results, [], i, nums)
        return results