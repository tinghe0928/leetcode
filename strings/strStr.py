class Solution:

    def strStr(self, haystack, needle):

        m =  len(haystack)
        n = len(needle)
        if n > m:
            return -1
        if needle == "":
            return 0
        i = 0
        j = 0
        while i < m:
            while i < m and haystack[i] != needle[j]:
                i += 1
            if (i+n-1) < m and haystack[i:i+n] == needle:
                return i
            else:
                i += 1
        return -1


haystack = "ffffffffff"
needle = "ll"
print(Solution().strStr(haystack, needle))