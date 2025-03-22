class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        m = n.bit_length() - 1  
        return (1 << (m + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << m))