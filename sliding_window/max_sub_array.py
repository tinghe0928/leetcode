class Solution:
    """
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
    主要思想，只有当sum[:i]-sum[:j]>0的时候，才会对最大和有帮助

    [num[0], num[1],......num[i]......num[n-1]]
    动态规划的是首先对数组进行遍历，当前位置i最大连续子序列和为 sum，sum起始值为0，历史最大子序列结果为 ans，ans起始值为num[0]
    如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
    如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
    每次比较 当前sum 和 历史ans的大小，将最大值置为ans，继续往后遍历，遍历结束返回结果
    时间复杂度：O(n)
    """
    @staticmethod
    def max_sub_array(nums):
        sum = 0
        history_max_sum = nums[0]
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            print("历史最大值以及当前最大值:",history_max_sum,sum)
            history_max_sum = max(history_max_sum,sum)
        return history_max_sum

    def maxSubArray(nums):
        pre_sum = 0
        ans = nums[0]
        for num in nums:
            pre_sum = max(pre_sum+num, num)
            print(pre_sum,ans)
            ans = max(pre_sum,ans)
        return ans

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = Solution.max_sub_array(nums)
    print("The max su array is:", result)




