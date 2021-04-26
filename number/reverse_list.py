class Solution:

    def reverseList(self, mylist):
        n = len(mylist)
        result = []
        for i in range(n-1, -1, -1):
            result.append(mylist[i])
        return result

