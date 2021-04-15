class Solution:

    @staticmethod
    def hash_search(nums):
        hashtable = []
        l = len(nums)
        for i in len(nums):
            hashtable.append(Solution.make_hash(nums[i]),l)


    @staticmethod
    def make_hash(num,l):
        return num%l




