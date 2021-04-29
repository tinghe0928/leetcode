class Solution:
    def fib_0(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Solution().fib(n-1) + Solution().fib(n-2)

    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        mylist = [None for i in range(n+1)]
        mylist[0] = 0
        mylist[1] = 1
        for i in range(2,n+1):
            mylist[i] = mylist[i-1] + mylist[i-2]
        return mylist[n]

n = 0
print(Solution().fib(n))
