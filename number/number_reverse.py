class Solution:

    @staticmethod
    def reverse(x):
        ab_x= abs(x)
        m = 0
        tmp = 0
        for i in str(ab_x):
            tmp += int(i)*pow(10, m)
            m += 1
        if x < 0:
            result = -tmp
        else:
            result = tmp
        if result < -pow(2,31) or result > pow(2,31) -1:
            return 0
        else:
            return result

    @staticmethod
    def reverse_better(x):
        y = abs(x)
        res = 0
        if x > 0:
            boundry = pow(2,31) - 1
        else:
            boundry = pow(2,31)
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        if x > 0:
            return res
        else:
            return -res


if __name__=="__main__":
    x = 123
    print(Solution.reverse_better(x))




