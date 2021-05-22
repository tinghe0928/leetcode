class Solution:
    def permutation(self, s):
        "全排列"
        if len(s) <= 1:
            return list(s)
        result = []
        for i in range(len(s)):
            if s[i] not in s[:i]:
                for j in self.permutation(s[:i]+s[i+1:]):
                    result.append(s[i]+j)
        return result


    def permute(self, nums):
        n = len(nums)
        result = []
        if n == 1:
            result.append(nums)
        for i in range(n):
            if nums[i] not in nums[:i] :
                for j in self.permute(nums[0:i]+nums[i+1:]):
                    result.append([nums[i]]+j)
        return result

# s = "aabc"
# print(Solution().permutation(s))
n = [1,1,1,3]
print(Solution().permute(n))


