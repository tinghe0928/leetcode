class Solution:
    def firstUniqChar(self, s: str):
        n = len(s)
        mydic = {}
        for i in range(n):
            if s[i] in mydic:
                mydic[s[i]] = n  # 赋予其等于一个不等于返回值的数值即可
            else:
                mydic[s[i]] = i
        for ele in mydic:
            if mydic[ele] != n:
                return mydic[ele]
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))


