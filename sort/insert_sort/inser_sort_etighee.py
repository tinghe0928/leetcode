class Solution:
    """
    leetcode上运行了一下，case通过率10/11，剩下一个超时失败
    核心在于如何将一个元素插入已经排好序的苏烈中去
    """
    @staticmethod
    def sortArray(nums):
        n = len(nums)
        if n > 1:
            for i in range(n-1):
                key = nums[i+1]
                for j in range(i, -1, -1):
                    while -1 < j < n and key < nums[j]:
                        nums[j+1] = nums[j]
                        j = j-1
                    nums[j + 1] = key
                    break
        return nums


if __name__=="__main__":

    lists=[1, 0, -1]
    print("排序前的序列为：", lists)
    sorted_lists = Solution().sortArray(lists)
    print("排序后的序列为：", sorted_lists)
