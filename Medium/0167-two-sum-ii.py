class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) solution

        left, right = 0, len(numbers) - 1

        while left <= right:
            summ = numbers[left] + numbers[right]

            if summ < target:
                left += 1
            elif summ > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        