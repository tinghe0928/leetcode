import pytest
class Solution:
    "当num_0>k时移动左指针更换起点, 在num_0<=k时移动右指针, 不断加长可能的子串长度"
    def longestOnes0(self, nums, K):
        res = 0
        L = 0                       #标准滑动窗口框架  左端点
        window_1_cnt = 0            #滑动窗口内1的个数
        for R in range(len(nums)):     #滑动窗口右端点
            if nums[R] == 1:
                window_1_cnt += 1
            window_0_cnt = R - L + 1 - window_1_cnt #滑动窗口内0的个数
            while window_0_cnt > K:     #判断条件，L右移
                if nums[L] == 1:
                    window_1_cnt -= 1
                else:
                    window_0_cnt -= 1
                L += 1
            res = max(res, R-L+1)

        return res

    def longestOnes1(self, a, k) -> int:
        n = len(a)
        l, r = 0, 0
        num_0 = 0
        res = 0
        while r < n:
            if a[r] == 0:
                num_0 += 1
            while num_0 > k:
                if a[l] == 0:
                    num_0 -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

    def longestOnes(self, nums, k):
        n = len(nums)
        left = 0
        right = 0
        count_0 = 0
        max_len = 0
        while right < n:
            if nums[right] == 0:
               count_0 += 1
            while count_0 > k:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums,k))



