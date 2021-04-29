class Solution:
    def mergeTwoLists(self, list1, list2):
        m = len(list1)
        n = len(list2)
        if list1[-1] <= list2[0]:
            return list1 + list2
        if list2[-1] <= list1[0]:
            return list2 + list1
        result = []
        i = j = 0
        while i < m and j < n:
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        if i == m:
            result = result.append(list2[j:])
        if j == n:
            result = result.append(list1[i:])
        return result

list1 = [1,2,3,4]
list2 = [2,3,4,6,7,9,11,115]
print(Solution().mergeTwoLists(list1, list2))





