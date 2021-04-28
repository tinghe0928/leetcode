class Solution:

    @staticmethod
    def addTwoNumbers(x,y):
        result = []
        m = 0
        for i in range(len(x)-1,-1,-1):
            m = m*10+x[i]
        n = 0
        for i in range(len(y)-1,-1,-1):
            n = n*10+y[i]
        print(m,n)
        num = m+n

        for i in str(num):
            result.append(int(i))
        return result


if __name__ == "__main__":
    x = [1,2,3]
    y = [1,2,3]
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(Solution.addTwoNumbers(l1,l2))

