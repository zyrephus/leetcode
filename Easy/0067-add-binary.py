class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # O(n) solution

        res = ""
        carry = 0

        a, b = a[::-1], b[::-1] # Reverse the strings for easier addition
        aLen, bLen = len(a), len(b)

        for i in range(max(aLen, bLen)): # Making sure we're looping over the larger number
            digitA = int(a[i]) if i < aLen else 0
            digitB = int(b[i]) if i < bLen else 0
            
            summ = digitA + digitB + carry
            if summ == 3:
                summ = 1
                carry = 1
            elif summ == 2:
                summ = 0
                carry = 1
            else:
                carry = 0
            
            res += str(summ)
        
        if carry: # If we need an extra place value
            res += "1"
        return res[::-1]
            