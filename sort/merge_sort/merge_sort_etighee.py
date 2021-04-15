class Solution:
    @staticmethod
    def sortArray(nums):
        n = len(nums)
        middle = n // 2
        if n > 1:
            left = Solution.sortArray(nums[:middle])
            right = Solution.sortArray(nums[middle:])
            print(left,right)
            return Solution.sort_two_array(left, right)
        return nums
    @staticmethod
    def sort_two_array(a,b):

        if a[-1] <= b[0]:
            for i in range(len(b)):
                a.append(b[i])
            return a
        elif b[-1] <= a[0]:
            for i in range(len(a)):
                b.append(a[i])
            return b
        else:
            # 方法1： 将两个有序序列合并的本质，其实就是将一个元素插入有序序列中去

            i = len(a) - 1
            print(a, b)
            for j in range(len(b)):
                a.append(b[j])
                while i > -1 and a[i] > b[j]:
                    a[i+1] = a[i]
                    i = i - 1

                a[i+1] = b[j]
                i = len(a) - 1

            return a



if __name__ == "__main__":
    a = [4, 5, 7, 1, 9, 0, 8]
    print("排序后的序列为：", Solution.sortArray(a))

