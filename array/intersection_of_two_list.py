class Solution:

    def intersection_all(self, nums1, nums2):
        "所有交际全部打印出来"
        result = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                print(j, i)
                tmp = []
                if nums1[i] == nums2[j]:
                    tmp.append(nums1[i])
                    m = i+1
                    n = j+1
                    while m < len(nums1) and n < len(nums2) and nums1[m] == nums2[n]:
                        tmp.append(nums1[m])
                        m += 1
                        n += 1
                    result.append(tmp)
                j += 1
        return result


    def intersection_chars(self, nums1, nums2):
        "只打印交集元素"
        result = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):

                if nums1[i] == nums2[j] and nums1[i] not in result:
                    result.append(nums1[i])
                j += 1
        return result

nums1 = [2,1,2,3,4]
nums2 = [3,2,3,4,5]

print(Solution().intersection_chars(nums1, nums2))
