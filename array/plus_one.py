class Solution:
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        num = num + 1
        tmp = []
        result = []
        while num != 0:
            i = num % 10
            tmp.append(i)
            num = num // 10
        n = len(tmp)
        for i in range(n):
            result.append(tmp[n-1-i])
        return result


num = [1,2,3]
print(Solution().plusOne(num))