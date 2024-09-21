class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # O(n) solution

        res = []
        
        curr = 1 # Always start with 1
        while len(res) < n:
            res.append(curr)

            # Traversing and checking if in bounds
            if curr * 10 <= n:
                curr *= 10
            else:
                # Check if in bounds or if curr has reached the last number
                while curr == n or curr % 10 == 9:
                    curr //= 10 # Pop back up
                curr += 1 # Adding 1 either way 

        return res