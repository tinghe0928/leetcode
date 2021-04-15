class Solution:

    @staticmethod
    def merge_sort(nums, left, right, target):
        mid = left + (right-left)//2
        if target == nums[mid]:
            return mid
        elif left <= right and target > nums[mid]:
            left = mid + 1
            return Solution.merge_sort(nums, left, right, target)
        elif left <= right and target < nums[mid]:
            right = mid - 1
            return Solution.merge_sort(nums, left, right , target)
        else:
            return -1


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 77
    target_index = Solution.merge_sort(nums, 0, len(nums)-1,target)
    if target_index is not -1:
        print("target", target, "在数组的第", target_index, "位")
    else:
        print("没有你要找的值")
