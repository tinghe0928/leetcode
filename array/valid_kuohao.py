class Solution:

    @staticmethod
    def isValid(s):
        "带非括号的字符的"
        mylist = []
        for i in range(len(s)):
            if s[i] not in ['{','}','(',')','[',']']:
                continue
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                mylist.append(s[i])
            elif len(mylist) != 0:

                if (mylist[-1] == '{' and s[i] == '}') or (mylist[-1] == '(' and s[i] == ')') or (mylist[-1] == '[' and s[i] == ']'):
                    mylist.pop()
                else:
                    return False
            else:
                return False
        return mylist == []

a = '{2399[88{4]78}'
print(Solution().isValid(a))