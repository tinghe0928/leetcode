class Solution:
    def jump(self, nums):
        n = len(nums)

        def find_next(start):
            "当前元素大于后续步长的时候，直接返回列表末尾"
            if start+nums[start] >= n-1:
                return n-1
            "max_sum下一步列表中最大的数"
            max_step = start+1
            max_step_value = nums[start+1]
            max_sum = max_step + max_step_value
            "找到最大元素的最远下标，为避免有相等的值，从远处开始遍历"
            for i in range(start+nums[start], start, -1):
                if i + nums[i] >= max_sum:
                    max_step = i
                    max_step_value = nums[i]
                    max_sum = max_step + max_step_value
            return max_step
        start = 0
        step = 0
        while start < n-1:
            next = find_next(start)
            print("start is ", start,'next is ',next)
            step += 1
            start = next
        return step


nums = [9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]
print(Solution().jump(nums))