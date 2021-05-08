class Solution:
    def longestCommonPrefix(self, strs):

        pre = ''
        index = 0
        flag = False
        while True:
            for i in range(len(strs)):
                if index < len(strs[i]) and strs[0][index] == strs[i][index] :
                    flag = True
                else:
                    print("this is False branch")
                    flag = False
                    break
            if flag:
                pre += strs[0][index]
                index += 1
            else:
                break
        return pre



strs = [""]
print(len(strs))
print(Solution().longestCommonPrefix(strs))