class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []

        def flip(k):
            l, r = 0, k - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        for target in range(n, 1, -1):
            i = arr.index(target)

            if i == target - 1:
                continue

            if i != 0:
                flip(i + 1)
                res.append(i + 1)
            flip(target)
            res.append(target)

        return res
        
