class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        ele = int()
        mydic = {}
        for num in nums:
            mydic[num] = mydic.get(num, 0) + 1
            if mydic[num] > n/2:
                ele = num
        return ele