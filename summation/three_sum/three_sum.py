#! /usr/bin/env python
# coding = utf-8

from two_sum.two_sum import TwoSum  # 需要将父目录summation mark directory as sources root
from sort.bubble_sort.bubble_sort import BubbleSort


class ThreeSum:

    @staticmethod
    def sum_of_three_nums(my_list, my_sum):
        """
        :param my_list: 输入的数组
        :param my_sum: 三数之和的和值
        :return: 返回输入数组中不重复的所有和为my_sum的三个数的列表
        """
        all_items = []
        my_len = len(my_list)
        if my_len > 2:  # 当数组长度大于等于3的时候，才会存在三数之和的等于my_sum，否则直接返回空结果列表
            BubbleSort.bubble_sort(my_list)  # 先将数组进行排序
            i = 0
            for i in range(my_len-1):
                if my_list[i] > my_sum:  # 当数组中最小的值比所求的和大，直接退出程序，返回空结果列表
                    print("当前数组中最小的值已经比所求的和大，直接退出程序")
                    return all_items
                if i > 0 and my_list[i] == my_list[i-1]:  # 对于重复元素：跳过，跳出当前循环，避免出现重复解
                    continue
                left = i + 1
                right = my_len -1
                while left < right:
                    if my_list[i] + my_list[left] + my_list[right] < my_sum:
                        left = left + 1
                    elif my_list[i] + my_list[left] + my_list[right] > my_sum:
                        right = right - 1
                    else:
                        while my_list[left] == my_list[left+1]:
                            left = left + 1
                        while my_list[right] == my_list[right-1]:
                            right = right-1
                        all_items.append([my_list[i], my_list[left], my_list[right]])
                        left = left + 1
                        right = right - 1
        return all_items


if __name__ == "__main__":
    test_list = [1, 2, 2, 2, 2, 3, 7, 8, 8]  # 1 需要去重， 2 一次遍历可能存在多组值
    test_sum = 11
    result = ThreeSum.sum_of_three_nums(test_list, test_sum)
    print("和为", test_sum, "的所有的三数组合为", result)

