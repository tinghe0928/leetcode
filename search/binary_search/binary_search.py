class Solution:
    """
    二分查找
    二分查找适用于已经排好序的序列
    """
    @staticmethod
    def search(nums, target):
        if len(nums) > 1:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left +((right - left) // 2)
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            return -1  # 若没有找到目标值，返回 -1
        elif len(nums) == 1 and nums[0] == target:
            return 0
        else:
            return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2
    target_index = Solution.search(nums, target)
    if target_index is not -1:
        print("tartget", target, "在数组的第", target_index, "位")
    else:
        print("没有你要找的值")