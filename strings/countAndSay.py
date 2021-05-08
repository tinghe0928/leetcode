class Solution:
    def countAndSay(self, n):
        def say_num(num):
            l =len(str(num))
            numb = ''
            count = 1
            key = str(num)[0]
            if l == 1:
                numb =  str(count)+str(num)[0]
            i = 1
            while i <l:
                if str(num)[i] == key:
                    count += 1
                else:

                    numb += str(count) + key

                    key = str(num)[i]
                    count = 1
                if i == l-1:
                    numb += str(count) + key

                i += 1

            return int(numb)

        mylist = [None for _ in range(n+1)]
        mylist[0] = 0
        mylist[1] = 1
        for i in range(2,n+1):
            mylist[i] = say_num(mylist[i-1])
        return mylist

n = 5
print(Solution().countAndSay(n))


