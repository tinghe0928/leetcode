import math
class Solution:

    @staticmethod
    def max_sub_array(nums):

        pre_sum = 0
        history_max = nums[0]
        for i in range(len(nums)):
            if pre_sum >= 0:
                pre_sum = pre_sum + nums[i]
            else:
                pre_sum = nums[i]
            history_max = max(pre_sum , history_max)
        return history_max

    @staticmethod

    def smallest_subarray_with_given_sum(arr,s):
        """
        和为K的子序的长度（size）
        """
        window_sum = 0
        min_length = 0
        window_start = 0

        for window_end in range(0, len(arr)):
            window_sum += arr[window_end]  # add the next element
            # shrink the window as small as possible until the 'window_sum' is smaller than 's'
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        return min_length


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution.max_sub_array(nums)
    print(Solution.smallest_subarray_with_given_sum(nums,3))
    print("The max su array is:", result)