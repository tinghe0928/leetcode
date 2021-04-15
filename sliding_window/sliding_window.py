# 可以看参考https://zhuanlan.zhihu.com/p/141072424

class Solution:
    """
    给定一个整数数组和一个整数 k，找到该数组中和为k的连续的子序的个数（有几个这样的子序列）
    """
    @staticmethod
    def subarraySum(nums, k):
        hashtable = {0:1}  # 对于一开始的情况，下标 0 之前没有元素，可以认为前缀和为 0，个数为 1 个
        ret = 0  # ret为计数器
        pre_sum = 0
        for num in nums:
            pre_sum = pre_sum + num
            hashtable[pre_sum] = hashtable.get(pre_sum, 0) + 1
            ret = ret + hashtable.get(pre_sum - k, 0)  # presum[:i] - presum[:j] == k <=> presum[i] - k = presum[j]
        print(hashtable)
        return ret


if __name__ == "__main__":
    nums = [1, 1, 1, 4]
    k = 6
    print(Solution.subarraySum(nums, 1))
