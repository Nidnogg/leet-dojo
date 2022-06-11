# Exceeds time limit.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:  
        results = []
        candidates.sort()
        def backtracking(results, path, depth, options):
            if(depth == 0):
                results.append(path[:])
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()
        combinations = []
        backtracking(combinations, [], 2, candidates)
        
        i = 0        
        while(i <= len(candidates)):
            combinations = []
            backtracking(combinations, [], i, candidates)
            for comb in combinations:
                sum = 0
                for elem in comb:
                    sum += elem
                if(sum == target):
                    if(comb in results): 
                        continue
                    else:
                        results.append(comb)       
            i += 1
        return results
                
//Includes repetitionclass Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:  
        results = []
        
        def backtracking(results, path, depth, options):
            if(depth == 0):
                results.append(path[:])
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()
        combinations = []
        backtracking(combinations, [], 2, candidates)
        print(combinations)
        # i = 0        
#         while(i <= len(candidates)):
#             combinations = []
#             backtracking(combinations, [], i, candidates)
#             for comb in combinations:
#                 print(comb)
#                 # sum = 0
#                 # for elem in comb:
#                 #     sum += elem
#                 # if(sum == target):
#                 #     results.append(comb)
#             i += 1
                
       
        
//Implementation of backtracking for combinations
//from https://nicksma.medium.com/combinations-and-permutations-with-an-intro-to-backtracking-d940683ea9de
class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        combinations = []
        
        def backtracking(results, path, depth, options):
            if depth == 0:
                results.append(path[:])
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()
                    
        backtracking(combinations, [], k, nums)
            
        return combinations

//Implementation of backtracking for combinations
//from https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination
vector<vector<int>>res;

vector<vector<int>> combine(int n, int k) {
    if (k <= 0 || n <= 0) return res;
    vector<int> track;
    backtrack(n, k, 1, track);
    return res;
}
​
void backtrack(int n, int k, int start, vector<int>& track) {
    // reach the bottom of tree
    if (k == track.size()) {
        res.push_back(track);
        return;
    }
    // note: i is incremented from start 
    for (int i = start; i <= n; i++) {
        // select
        track.push_back(i);
        backtrack(n, k, i + 1, track);
        // deselect
        track.pop_back();
    }
}   