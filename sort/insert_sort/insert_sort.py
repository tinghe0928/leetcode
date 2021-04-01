#!/usr/bin/env python
# coding=utf-8


class Solution:

    @staticmethod
    def sortArray(nums):
        n = len(nums)
        if n > 1:
            lists = [nums[0]]
            start = 1
            while start < n:
                while start < n and lists[-1] < nums[start]:  # 若nums[start]比lists[-1](lists中最大的值)大，直接将nums[start] append 到list后面
                    lists.append(nums[start])
                    start += 1
                if start < n:  # 当涉及到 +1 或者 -1 的时候都应该考虑数组是否溢出，如[1,2,3]有序序列就会碰到这种问题
                    key = nums[start]
                else:
                    break
                lists.append(key)  # 先将要插入的值append到lists中，然后对lists进行排序
                j = start
                while j > 0 and lists[j] < lists[j-1]:
                    lists[j],lists[j-1] = lists[j-1],lists[j]
                    j -= 1
                start += 1  # 排完lists之后，继续将start后移，继续将nums[start]插入到有有序序列lists中去
            return lists
        return nums


if __name__=="__main__":

    lists=[1,2,3,4]  # [30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：", lists)
    sorted_lists = Solution().sortArray(lists)
    print("排序后的序列为：", sorted_lists)