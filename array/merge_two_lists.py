class Solution:
    def mergeTwoLists(self, list1, list2):
        "开辟新的空间+双指针"
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
            result += list2[j:]
        if j == n:
            result += list1[i:]
        return result

    def merge(self, list1, m, list2, n):
        "开辟新的空间+双指针"
        list1 = list1[0:m]
        list2 = list2[0:n]
        print(list1)
        print(list2)
        if list1[-1] <= list2[0]:
            return list1 + list2
        if list2[-1] <= list1[0]:
            return list2 + list1
        result = []
        i, j = 0, 0
        while i < m and j < n:
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        if i == m:
            result += list2[j:]
        if j == n:
            result += list1[i:]
        return result

    def merge1(self, list1, m, list2, n):
        "不开辟新的空间，将元素插入到已排列序列中去,del多余的元素"
        if n == 0:
            return list1[0:m+n]
        if m == 0:
            list1[0:m + n] = list2[0:n]
            return list1[0:m + n]
        if list1[m - 1] <= list2[0]:
            list1[0:m + n] = list1[0:m] + list2[0:n]
            return list1[0:m + n]
        if list2[n - 1] <= list1[0]:
            list1[0:m + n] = list2[0:n] + list1[0:m]
            return list1[0:m + n]
        i, j = 0, 0
        while j < n:
            print("this is last")
            while i < len(list1) and j < len(list2) and list1[i] <= list2[j]:
                if i < m + j:
                    i += 1
                else:
                    list1[m + j:] = list2[j:n]
                    return list1[0:m + n]
            list1[i + 1:] = list1[i:]
            if i < m + n and j < n:
                list1[i] = list2[j]
            j += 1
        del list1[m+n : ]
        return list1[0: m + n]


list1 = [1,2,4,5,6,0]
list2 = [3]
m = 5
n = 1

# print(Solution().mergeTwoLists(list1, list2))
print(Solution().merge1(list1, m, list2, n))





