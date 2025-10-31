class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)

        return res

# Not optimal solution (involves XOR which is too complicated...)
