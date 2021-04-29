class Solution:
    @staticmethod
    def longestPalindrome(s):
        n = len(s)
        if n < 2:
            return s

        ##############中心扩展法，最直观的方法
        def center_spread(L: int, R: int) -> str:
            while 0 <= L and R < n and s[L] == s[R]:
                L = L - 1
                R = R + 1
            return s[L+1: R]  # 包含L+1&不包含R

        result = s[0]
        max_len = 1

        for i in range(n):
            odd_str = center_spread(i, i)
            even_str = center_spread(i, i + 1)

            if len(odd_str) > len(even_str):  # 若长度为奇数的长
                if len(odd_str) > max_len:
                    max_len = len(odd_str)
                    print("odd")
                    result = odd_str
            else:  # 若长度为偶数的长
                if len(even_str) > max_len:
                    max_len = len(even_str)
                    print("even")
                    result = even_str
        return result

# class Solution:
#     @staticmethod
#     def longestPalindrome(s):
#         n = len(s)
#         if n <= 1:
#             return s
#         def find_palindrome(mystring,l,r):
#             tmp = []
#             while 0<=l and r < len(mystring) and mystring[l] == mystring[r]:
#                 l -= 1
#                 r += 1
#             tmp = mystring[l+1:r]
#             return tmp
#         max_palindrome = s[0]
#         for i in range(len(s)):
#             palindrome_odd = find_palindrome(s,i,i)
#             palindrome_even = find_palindrome(s,i,i+1)
#             # print('palindrome_odd, palindrome_even', palindrome_odd,'*', palindrome_even)
#             if len(palindrome_odd) >= len(palindrome_even):
#                 max_tmp = palindrome_odd
#             else:
#                 max_tmp = palindrome_even
#             if len(max_tmp) >= len(max_palindrome):
#                 max_palindrome = max_tmp
#         return max_palindrome


if __name__ == "__main__":
    x = "12332b"
    print(Solution.longestPalindrome(x))