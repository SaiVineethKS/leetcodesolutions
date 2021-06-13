class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            sum = 0
            while n:
                sum += (n % 10) * (n % 10)
                n //= 10
            n = sum
        return n == 1
        #     return self.isHappy(sum(int(i)**2 for i in str(n)))


