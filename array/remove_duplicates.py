class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return n
        i = 0
        j = 1
        while j < n :
            while j < n and nums[j] == nums[j-1]:
                j += 1
            if j < n:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return nums[0:i+1]

    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return n
        result = [nums[0]]
        i = 1
        while i < n:
            while i < n and nums[i] == nums[i-1]:
                i += 1
            if i < n:
                result.append(nums[i])
                i += 1
        print("****",result)
        return len(result)


nums = [1,1,2]
print(Solution().removeDuplicates(nums))