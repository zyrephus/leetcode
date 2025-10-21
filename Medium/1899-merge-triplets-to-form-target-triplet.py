class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()
        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            for i, num in enumerate(triplet):
                if num == target[i]:
                    valid.add(i)

        return len(valid) == 3
