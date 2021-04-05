class Solution:

    @staticmethod
    def sortArray(nums):
        # 1. 首先排除特殊待排序的序列，如空序列或者长度为1的序列
        n = len(nums)
        middle = n // 2
        if n > 1:
            left = Solution.sortArray(nums[:middle])
            right = Solution.sortArray(nums[middle:])
            return Solution.merge_sort(left, right)
        return nums

    @staticmethod
    def merge_sort(a, b):
        c = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        if i == len(a):
            for k in b[j:]:
                c.append(k)
        if j == len(b):
            for k in a[i:]:
                c.append(k)
        return c


if __name__ == "__main__":
    a = [4, 5, 7, 1, 9, 0, 8]
    print("排序后的序列为：", Solution.sortArray(a))



