class Solution:

    @staticmethod
    def binarySearch(nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid-1
        return -1


if __name__ == "__main__":
    nums = [1]
    target = 1
    target_index = Solution.binarySearch(nums, target)
    if target_index is not -1:
        print("target", target, "在数组的第", target_index, "位")
    else:
        print("没有你要找的值")