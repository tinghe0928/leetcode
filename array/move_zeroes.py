class Solution:

    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] == 0 and i+1 < n:
                for j in range(i+1,n):
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
                    j += 1
        return nums


nums = [0, 0, 0, 3, 12]
print(Solution().moveZeroes(nums))


"""
自己的解题思路，从最后一个数开始遍历，如果元素等于0，则冒泡和后面的数进行交换，直至交换到数组末尾
"""

