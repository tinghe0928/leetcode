class Solution:

    @staticmethod
    def solution(nums,k):
        "Pair with Target Sum"
        if len(nums) > 1:
            result = []
            dic = {}
            for i in range(len(nums)):
                if nums[i] in dic:
                    result.append((dic[nums[i]], i))

                dic[k-nums[i]] = i
        return result


if __name__ == "__main__":

    test_list = [2, 7, 11, 2, 15, 13, 0, 0, 13]
    test_sum = 13
    my_index = Solution.solution(test_list, test_sum)
    if my_index == []:
        print("不存在这样的两数")
    else:
        print('当前数组为:', test_list, "和为:", test_sum, "的数组下标为:", my_index)



