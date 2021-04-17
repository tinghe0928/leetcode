
class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s):

        n = len(s)
        if n < 2:
            return len(s)

        max_len = 1
        i = 0
        while i < n:
            j = i + 1
            my_dic = {s[i]: i}
            while j < n and s[j] not in my_dic:
                my_dic[s[j]] = j
                j += 1
            max_len = max(max_len, j-i)
            if j < n:
                i = my_dic[s[j]]+1
            else:
                return max_len


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        n = len(s)
        if n<2:
            return n
        i = 0
        j = 1
        # 设置初始窗口大小为1
        max_len = 1
        while j<n:
            while j<n and s[j] not in s[i:j]:
                j += 1
            max_len = max(max_len, j-i)
            if j != n:
                # 计算头指针的移动步数
                print(s[i:j].index(s[j]))
                i = i + s[i:j].index(s[j])+1
        return max_len







if __name__ == "__main__":
    s = "pwwkew"#"abcdeabcdefghii"
    print(Solution.lengthOfLongestSubstring(s))





