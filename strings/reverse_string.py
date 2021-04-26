class Solution:
    def reverseString(self, slist):
        print(slist)
        n = len(slist)
        left = 0
        right = n - 1 - left
        while left < right:
            slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right = n - 1 - left
        