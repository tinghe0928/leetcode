class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <= 1:
           return n
        i = 0
        max_len = 1
        while i< n:
            res = {s[i]:i}
            j = i + 1
            while j < n and s[j] not in res:
                res[s[j]] = j
                j += 1
            max_len = max(max_len, j-i)
            if j == n:
                return max_len
            i = res[s[j]] + 1


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
