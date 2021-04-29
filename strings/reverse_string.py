class Solution:
    def reverseString(self, slist):
        "有两种方法，一种从序列末尾遍历，一种就是首位相应位置互换"
        print(slist)
        n = len(slist)
        left = 0
        right = n - 1 - left
        while left < right:
            slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right = n - 1 - left
        return self

s = [1, 2, 3]
Solution().reverseString(s)
print(s)
