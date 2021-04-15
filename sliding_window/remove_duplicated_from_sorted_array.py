class Solution:

    @staticmethod
    def removeDuplicates_1(nums):
        """
        新开辟一个空间
        """
        if len(nums) > 1:
            my_list = []
            my_list.append(nums[0])
            i = 1
            while i <= len(nums)-1:

                while i <= len(nums)-1 and nums[i] == nums[i-1]:
                    i += 1
                if i <=len(nums) -1:
                    my_list.append(nums[i])
                    i += 1
            return len(my_list),my_list
        return len(nums),nums

    @staticmethod
    def removeDuplicates(nums):
        """
        不新开辟空间
        """
        if len(nums) > 1:

            i = 0
            j = 1
            while j <= len(nums) - 1:

                while 1 <=j <= len(nums)-1 and nums[j] == nums[j - 1]:
                    j += 1
                if j <= len(nums)-1:
                    nums[i+1] =nums[j]
                    i += 1
                    j += 1
            return len(nums[0:i+1]),nums[0:i+1]
        return len(nums), nums


if __name__ == "__main__":
    nums = [1, 3, 11, 11, 18]
    print(Solution.removeDuplicates_1(nums))