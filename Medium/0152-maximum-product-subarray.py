class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn, maxx = 1, 1
        res = max(nums)

        for num in nums:
            if num == 0:
                minn, maxx = 1, 1
                continue
            
            temp = minn * num # Need temp as min() updates in-place

            minn = min(num, maxx * num, minn * num)
            maxx = max(num, maxx * num, temp)

            res = max(res, maxx)

        return res
    
