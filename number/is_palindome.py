class Solution:


    def isPalindrome(self,x):
        s = str(x)
        n = len(s)
        mid = n // 2
        result = True
        left = mid - 1
        if n % 2 == 1:
            right = mid + 1
        else:
            right = mid
        while 0 <= left and right <= n-1:
            result = result and (s[left] == s[right])
            left -= 1
            right += 1
        if left == -1 and right == n:
            return result
        return False


x= 1000021
print(Solution().isPalindrome(x))
print(Solution().isPalindrome(x))