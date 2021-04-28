class Solution:

    def removeDuplicates(self,s):
        n = len(s)
        slist = []
        if n < 2:
            return s
        else:
            i = 0
            while i < n:
                slist.append(s[i])
                #print(slist,i)
                j = i+1
                if j < n and s[j] == s[i]: # 如果是重复的数字全部删除,如qqq = ''用while ，如果偶数重复.奇数保留aa=''&aaa='a'就是if
                    j += 1
                if j - i == 1:
                    i += 1
                else:
                    print(slist)
                    slist = slist[0:-1] #这个是什么意思？去掉当前slist的最后以为
                    print(slist)
                    i = j
            s = ''.join(slist)
            n1 = len(s)
        if n == n1:
            return s
        else:
            return Solution().removeDuplicates(s)


s = "abbaca"#'adfjkahfjahfuierdsdd'

print(Solution().removeDuplicates(s))