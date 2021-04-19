class Solution:

    @staticmethod
    def permute(nums):

        mylist = []

        def permutations(arr, start, end):
            if start == end:
                print(arr)
                mylist.append(arr)
            if start != end:
                for i in range(start, end):
                    arr[i], arr[start] = arr[start], arr[i]
                    permutations(arr, start + 1, end)
                    arr[i], arr[start] = arr[start], arr[i]

        permutations(nums, 0, len(nums))
        return mylist

mylist =[]
arr = ["a", "b", "c"]
arr[0],arr[1] = arr[1],arr[0]
mylist.append(arr[:])
print(mylist)
print(">>>>>>>>>>>>>>>")
print(Solution.permute(arr))

