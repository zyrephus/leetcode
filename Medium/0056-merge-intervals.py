class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log(n)) solution

        # Sort by the first element of each interval
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            # Add the first interval
            # Also checks if current interval doesn't need to be merged
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # Merging
            else:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]

        return res