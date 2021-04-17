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


if __name__ == "__main__":
    x = "123321"
    print(Solution.longestPalindrome(x))