class Solution:

    def threeSum(self, nums):
        n = len(nums)
        result = []
        if n < 3:
            return []
        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        "对于已经排好序的序列"
        i = 0
        while i < n:
            if nums[i] > 0:
                return result
            while i < n and nums[i] in nums[:i]:
                i += 1
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    print(i, left, right)
                    while left+1 < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right - 1 and nums[right] == nums[right-1]:
                        right -= 1
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
            i += 1
        return result


mylist = [0, 0, 0]
print(Solution().threeSum(mylist))

