# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci sequence
        a, b = 1
        for i in range(n):
            temp = b
            b = a + b
            a = temp
        return a