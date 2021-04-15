#!/usr/bin/env python
# coding = utf-8
import sys
sys.setrecursionlimit(1000000)

class Solution(object):

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort_bp(self, lists, i, j):
        """本质感觉是双指针+三数交换"""
        if i >= j:
            return lists
        key = lists[i]
        low = i
        high = j
        while i < j:
            while i < j and lists[j] >= key:  # 往左循环，直到找到第一个小于基准值的j,将此值移到左边
                j -= 1
            lists[i] = lists[j]
            while i < j and lists[i] <= key:  # 往右循环，直到找到第一个大于基准值的i，将此值移到右边
                i += 1
            lists[j] = lists[i]
        lists[i] = key  # 将基准值放到左右值（也就是最后i与j相遇的位置）中间
        self.quick_sort(lists, low, i-1)
        self.quick_sort(lists, i+1, high)
        return lists

    def quick_sort(self, lists, i, j):
        """本质感觉是双指针+两数交换"""
        if i >= j:
            return lists
        key = lists[i]
        low = i
        high = j
        while i < j:
            while i < j and lists[j] >= key:  # 往左循环，直到找到第一个小于基准值的j,将此值移到左边
                j -= 1
            lists[i],lists[j] = lists[j],lists[i]
            while i < j and lists[i] <= key:  # 往右循环，直到找到第一个大于基准值的i，将此值移到右边
                i += 1
            lists[j],lists[i] = lists[i],lists[j]
        self.quick_sort(lists, low, i-1)
        self.quick_sort(lists, i+1, high)
        return lists


if __name__=="__main__":

    lists=[100, 999, 6, 6, 9, -1, 3, 3, -100]#[30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：", lists)
    sorted_lists = Solution().sortArray(lists)
    print("排序后的序列为：", sorted_lists)
