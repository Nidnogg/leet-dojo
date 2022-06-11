class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(results, path, depth, options):
            if(depth == 0):
                results.append(path[:])
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()
        combinations = []
        backtracking(combinations, [], k, range(1,n+1))
        return combinations
        