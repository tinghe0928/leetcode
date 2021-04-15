class Solution:

    def heapSort(nums):
        n = len(nums)


        # Build a maxheap.
        # 构建大顶堆需要有三个元素，序列，序列的长度，序列元素的index
        # 构建大顶堆需要从上往下构建，但是调整大顶堆可以从下往上调整
        for i in range(n//2 -1, -1, -1):  # 根据二叉树/完全二叉树的特性，含有叶子节点的最大的元素是 len//2 -1,所以构建大顶堆，是从 i -- > 0 构建的
            Solution.heapify(nums, n, i)

            # 一个个交换元素
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # 交换
            Solution.heapify(nums, i, 0)   # 调整剩下的序列为大顶堆

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i
        # + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 交换
            Solution.heapify(arr, n, largest)

"""
1. 对于一个长为n的序列，首先用将长为n的序列构建成大顶堆，即函数heapify(nums, n, i) i从倒数第一个非叶子节点（len//2 -1）开始构建即可
2. 构建成的大顶堆，根元素必然是最大值，根元素nums[0]和最后一个元素nums[i]交换，即完成最大值在序列末尾（升序排序）
3. 由于交换了位置，剩下的n-1个数，先调成大顶堆
4. 重复以上步骤，知道完成所有元素升序排序
"""