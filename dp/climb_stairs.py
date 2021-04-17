class Solution:

    @staticmethod
    def climbStairs(n):
        """暴力法，会超时"""
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return Solution.climbStairs(n-1) + Solution.climbStairs(n-2)


class Solution:

    @staticmethod
    def climbStairs(n):
        a =[None for i in range(n+1)]
        a[0] = 1
        a[1] = 1
        for i in range(2,n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]


n = 8
print(Solution.climbStairs(2))
