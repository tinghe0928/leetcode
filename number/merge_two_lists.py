class Solution:

    def mergeTwoLists(self, list1, list2):
        m = len(list1)
        n = len(list2)
        result = []
        if list1[-1] <= list2[0]:
            return list1 + list2
        if list2[-1] <= list1[0]:
            return list2 + list1
        i = j = 0
        while i < n and j < n:
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        if i == n:
            result += list2[j:n]
        if j == m:
            result += list1[i:n]
        return result


list1 = [1]
list2 = [1, 3, 4]
print(Solution().mergeTwoLists(list1, list2))

