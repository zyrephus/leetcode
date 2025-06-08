class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr[:])
                return

            if total > target or i >= len(candidates):
                return 

            # Include candidates[i]
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            curr.pop()

            # Skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1 , curr, total)

        backtrack(0, [], 0)

        return res
      
