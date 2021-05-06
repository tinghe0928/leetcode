class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if k == 0 or n <= 1:
            return nums
        k = k % n
        if k == 0:
            return nums
        nums[k:n], nums[0:k] = nums[0:(n-k)], nums[-k:]



    def rotate1(self, nums, k):
        n = len(nums)
        if k == 0 or n <= 1:
            return nums
        tmp_list = [None for _ in range(n)]
        for i in range(n):
            tmp_list[(i+k)%n] = nums[i]
        return tmp_list






nums = [1, 2]
k = 2
print(Solution().rotate(nums, k))



