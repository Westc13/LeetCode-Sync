class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n-1)) == 0 and (n - 1) % 3 == 0
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1