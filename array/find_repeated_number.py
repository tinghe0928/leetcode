class Solution:
    @staticmethod
    def findRepeatNumber(nums):
        n = len(nums)
        mydic = {}
        for i in range(n):
            if nums[i] not in mydic:
                mydic[nums[i]] = 1
            else:
                return nums[i]


numbers = [1, 2, 3, 4, 5, 3, 7]
print(Solution.findRepeatNumber(numbers))