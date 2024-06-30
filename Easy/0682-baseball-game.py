class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # O(n) solution

        record = [] # Stack approach
        for c in operations:
            if c == '+':
                record.append(record[-1] + record[-2])
            elif c == 'D':
                record.append(record[-1] * 2)
            elif c == 'C':
                record.pop()
            # Guaranteed a number
            else:
                record.append(int(c))

        return sum(record)