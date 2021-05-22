class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ''
        elif n == 1:
            return strs[0]
        result = strs[0]

        def common(s1, s2):
            if s1 == '' or s2 == '':
                return ''
            if len(s1) < len(s2):
                s1 = s1[0:len(s2)]
            i = 0
            while i < len(s1):
                print(i)
                while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                    i += 1
                break
            return s1[0:i]

        for i in range(1, n):
            result = common(result, strs[i])
        return result



strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))