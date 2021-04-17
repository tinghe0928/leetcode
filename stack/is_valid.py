class Solution:

    @staticmethod
    def is_valid(s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()','')
        return s == ''

    @staticmethod
    def is_valid_1(s):
        list=[]
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                list.append(s[i])
            elif len(list) != 0:
                if (list[-1] == '{' and s[i] == '}') or (list[-1] == '(' and s[i] == ')') or (list[-1] == '[' and s[i] == ']'):
                    list.pop()
                else:
                    return False
            else:
                return False
        print(list)
        return list == []


if __name__ == "__main__":
    s = "[)]"
    my_bool = Solution.is_valid_1(s)
    print("s is:", my_bool)

