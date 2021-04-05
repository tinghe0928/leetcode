#!/usr/bin/env python
# coding = utf-8


class BubbleSort:

    @staticmethod
    def bubble_sort(my_list):
        my_len = len(my_list)
        if my_len > 1:
            for i in range(my_len-1):
                for j in range(my_len-1-i):
                    if my_list[j] > my_list[j+1]:
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        return my_list

    @staticmethod
    def bubble_sort_1(my_list):
        n = len(my_list)
        if n > 1:
            for i in range(n-1):
                j = 0
                while j < n-1-i:
                    if my_list[j] > my_list[j+1]:
                        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    j += 1
        return my_list


if __name__ == "__main__":
    test_list = [100, 1, 6, 9, -1, 3, 3, -100]
    BubbleSort.bubble_sort_1(test_list)
    print("排序后的列表为：", test_list)