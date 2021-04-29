class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        mylist = []
        if nums1 == []:
            result = nums2
        elif nums2 == []:
            result = nums1
        elif nums1[-1] <= nums2[0]:
            result = nums1 + nums2
        elif nums2[-1] <= nums1[0]:
            result = nums2 + nums1
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                mylist.append(nums1[i])
                i += 1
            else:
                mylist.append(nums2[j])
                j += 1
        if i == m:
            result = mylist + nums2[j:]
        if j == n:
            result = mylist + nums1[i:]
        mid = (m + n) // 2
        if (m+n) % 2 == 0:
            return (result[mid-1]+result[mid])/2
        else:
            return  result[mid]


        

        




nums1 = [1, 2, 3, 4, 5, 3, 7, 8]
nums2 = [1, 2, 3, 4, 5, 3, 7, 8]
print(Solution().findMedianSortedArrays(nums1, nums2))