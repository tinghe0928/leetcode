class Solution:

    def permutation(self, s):
        s = list(s)
        n = len(s)
        result =[]

        def permutate(s, start, end):
            if start == end:
                res = ''
                for i in range(len(s)):
                    res += s[i]
                "去重"
                if res not in result:
                    return result.append(res)
            for i in range(start, end):
                s[start], s[i] = s[i], s[start]
                permutate(s, start+1, end)
                s[start], s[i] = s[i], s[start]
        permutate(s, 0, len(s))
        return result


class Solution1:

    def permutation1(self, s):

        # 如果字符串只有一个字符，直接输出
        if len(s) <= 1:
            return list(s)
        res = []
        # 每次取出字符串中的一个字符
        for i in range(len(s)):
            # 取出的字符串必须与之前的不同
            if s[i] not in s[:i]:
                # 再与剩下字符的全排列连接即可
                for j in self.permutation1(s[:i] + s[i + 1:]):
                    print(s[i],j)
                    res.append(s[i] + j)
        return res


s = "abc"  # "aab"
print(Solution1().permutation1(s))

