# 可以看参考https://zhuanlan.zhihu.com/p/141072424
from sort.quick_sort.quick_sort import Solution as SortSolution


class Solution:
    """
    给定一个整数数组和一个整数 k，找到该数组中和为k的连续的子数组的个数
    本质是找出sum[i,j]= sum[:i] - sum[:j]=k ===> sum[:j] = sum [:i] - k 满足这样的条件的组合有多少个

    另外还有一个暴力解法，循环序列种的每一个元素，计算这个元素的每一个子序列的和&与k做比较
    """
    @staticmethod
    def subarraySum(nums, k):
        hashtable = {0:1}  # 对于一开始的情况，下标 0 之前没有元素，可以认为前缀和为 0，个数为 1 个
        ret = 0
        pre_sum = 0
        for num in nums:
            pre_sum = pre_sum + num
            ret = ret + hashtable.get(pre_sum - k, 0)  # prefix[i] - prefix[j] == k <=> prefix[i] - k = prefix[j]
            hashtable[pre_sum] = hashtable.get(pre_sum, 0) + 1
            print(hashtable)
        return ret


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    Solution.subarraySum(nums, k)
