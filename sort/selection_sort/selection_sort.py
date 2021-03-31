#!/usr/bin/env python
# coding = utf-8


class SelectionSort:

    @staticmethod
    def selection_sort(my_list):
        my_len = len(my_list)
        if my_len > 1:
            for i in range(my_len):
                min_index = i
                for j in range(i+1, my_len):  # 快速排序的重点是在后面的数组中找出最小的值的下标，然后和my_list[i]进行调换
                    if my_list[j] < my_list[min_index]:
                        min_index = j
                my_list[i], my_list[min_index]  = my_list[min_index], my_list[i]
        return my_list


if __name__ == "__main__":
    test_list = [100, 1, 6, 6, 9, -1, 3, 3, -100]
    SelectionSort.selection_sort(test_list)
    print("排序后的列表为：", test_list)