class Solution:

    @staticmethod
    def permute(nums):
        "全排列"
        mylist = []

        def permutations(arr, start, end):
            if start == end:
                print(arr)
                mylist.append(arr)
            for i in range(start, end):
                arr[i], arr[start] = arr[start], arr[i]
                permutations(arr, start + 1, end)
                arr[i], arr[start] = arr[start], arr[i]

        permutations(nums, 0, len(nums))
        return mylist

mylist =[]
arr = ["a", "a", "c"]
arr[0],arr[1] = arr[1],arr[0]
mylist.append(arr[:])
print(mylist)
print(">>>>>>>>>>>>>>>")
print(Solution.permute(arr))

