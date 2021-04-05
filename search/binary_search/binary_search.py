class Solution:

    @staticmethod
    def search(nums:list, target:int, start) -> int:

        if len(nums) > 1:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
        else:
            return None


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 12
    target_index = Solution.search(nums, target, 0)
    if target:
        print("tartget", target, "在数组的第", target_index, "位")
    else:
        print("没有你要找的值")