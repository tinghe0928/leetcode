class Solution:

    def mySqrt(self, x):
        l = 0
        r = x
        ans = -1
        while l <= r:
            mid = (l + r) // 2  # 只需要比较中间元素 mid 的平方与 x 的大小关系，并通过比较的结果调整上下界的范围
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

print(Solution().mySqrt(8))