class Solution:

    @staticmethod
    def sortedSquares(nums):

        "nums为非递减数列"

        tmp = []
        if nums[-1] <= 0:
            for i in range(len(nums)-1,-1,-1):
                tmp.append(nums[i])
            nums = tmp
        if nums[-1] <= 0 or nums[0] >= 0:
            for i in range(len(nums)):
                nums[i] = nums[i]*nums[i]

            return nums

        else:
            i = 0
            while nums[i] < 0:
                i += 1
            j = i-1

            while j >= 0 and i <= len(nums)-1:
                if nums[i]*nums[i] < nums[j]*nums[j]:
                    tmp.append(nums[i]*nums[i])
                    i += 1
                else:
                    tmp.append(nums[j] * nums[j])
                    j -= 1
            print(i,j)
            if j == -1:
                for k in range(i,len(nums),1):
                    tmp.append(nums[k]*nums[k])
            if i == len(nums):
                for k in range(j,-1,-1):
                    tmp.append(nums[k]*nums[k])
            return tmp












if __name__ == "__main__":
    nums1 = [-4]
    nums2 = [-4,-3,-2,-1]
    nums3 = [-4, -3, -2, -1, 0, 1, 2, 3,6,7]
    nums4 = [0, 1, 2, 3]

    print(Solution.sortedSquares(nums1))
    print(Solution.sortedSquares(nums2))
    print(Solution.sortedSquares(nums3))
    print(Solution.sortedSquares(nums4))

