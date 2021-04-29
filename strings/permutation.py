class Solution:
    def permutation(self, s):
        "全排列"
        if len(s) <= 1:
            return list(s)
        result = []
        for i in range(len(s)):
            if s[i] not in s[:i]:
                for j in self.permutation(s[:i]+s[i+1:]):
                    result.append(s[i]+j)
        return result



