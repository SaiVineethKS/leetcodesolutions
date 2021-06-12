class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            numrev = -int(str(abs(x))[::-1])
        else:
            numrev = int(str(abs(x))[::-1])
        return numrev if numrev in range(-2**31, 2**31) else 0