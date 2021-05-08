class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        if nums[0] >=0 or nums[-1] < 0:
            return nums[-1]*nums[-2]*nums[-3]
        if nums[-1] ==0:
            return 0
        max1 = nums[0]*nums[1]*nums[-1]
        max2 = nums[-1]*nums[-2]*nums[-3]
        max_num = max(max1,max2)
        return max_num