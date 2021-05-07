class Solution:
    def isPalindrome(self, s):
        n = len(s)
        i = 0
        j = n-1
        result = True
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                result = False
                break
        return result


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))