class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # same index i because we can reuse the same element
                backtrack(i, path, total + candidates[i])
                path.pop()  # backtrack
        
        backtrack(0, [], 0)
        return result
