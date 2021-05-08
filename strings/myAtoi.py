class Solution:
    def myAtoi(self, s):
        n = len(s)
        i = 0
        key = ""
        num = 0
        while i < n:
            while i<n and s[i] == " ":
                i += 1
            if i < n and (s[i].isalpha() or s[i])== ".":
                return num
            if i<n and (s[i] == "-" or s[i]== "+"):
                key = s[i]
                i += 1
            j = i
            while i<n and s[i].isdigit():
                i += 1
            try:
                num = int(key + s[j:i])
            except:
                print("this is exception")
                num = 0
            if num < -pow(2,31):
                num = -pow(2,31)
            if num >= pow(2,31):
                num = pow(2,31) -1
            break
        return num


s = " -42"

print(Solution().myAtoi(s))

