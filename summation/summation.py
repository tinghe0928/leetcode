#!/usr/bin/env python
# coding=utf-8


class Summation(object):

    @classmethod  # 类函数(@classmethod):定义类方法，可以通过类(直接用类名)或者实例（需要先实例化这个类）调用，方法的第一个参数是class对象(这个时候就不是self,而是cls)
    def sum_of_two_nums(cls, cls_list, cls_sum):
        all_items = []
        for i in range(len(cls_list)):
            key = cls_sum - cls_list[i]
            # print("当前key的值是：", key)
            for j in range(i+1, len(cls_list)):
                # print("当前j对应的下标和值分别是：", [j, cls_list[j]])
                if cls_list[j] == key:
                    all_items.append([i, j])
        return all_items

    @classmethod
    def sum_of_three_nums(cls, cls_list, cls_sum):
        all_items = []
        for i in range(len(cls_list)):
            key = cls_sum - cls_list[i]
            sub_cls_list = cls_list[i+1:len(cls_list)]  # 拿出第i个数的值，截取第i+1及之后的值作为 sub list, 然后返回两函数之和的函数
            sub_index = cls.sum_of_two_nums(sub_cls_list, key)  # 返回两数之和的下表列表，若没有sum=key, 则返回空列表
            if len(sub_index) > 0:
                for j in range(len(sub_index)):
                    sub_index[j] = [h + (i+1) for h in sub_index[j]]  # 以下标i为基准，sub list 在 cls_list中的下表位置应该需要加上(i+1)
                    sub_index[j].insert(0, i)  # 加上三个数的第一个数的下标位置
                    all_items.append(sub_index[j])
        return all_items


my_list = [1, 2, 3, 4, 5, 7, 7]
my_sum = 6
my_index = Summation.sum_of_two_nums(my_list, my_sum)
print('当前数组为:', my_list, "和为:", my_sum, "的数组下标为:", my_index)
my_sum = 8
my_index = Summation.sum_of_three_nums(my_list, my_sum)
print('当前数组为:', my_list, "和为:", my_sum, "的数组下标为:", my_index)
