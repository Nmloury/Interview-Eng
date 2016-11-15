class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        idx1 = 0
        idx2 = 0
        L = []
        while idx1 < len(nums1) or idx2 < len(nums2):
            if not idx1 < len(nums1):
                L.append(nums2[idx2])
                idx2 += 1
            elif not idx2 < len(nums2):
                L.append(nums1[idx1])
                idx1 += 1
            else:
                if nums1[idx1] > nums2[idx2]:
                    L.append(nums2[idx2])
                    idx2 += 1
                else:
                    L.append(nums1[idx1])
                    idx1 += 1
        if len(L) % 2 == 1:
            return L[len(L) / 2]
        else:
            return (L[len(L) / 2] + L[(len(L) / 2) - 1]) / 2
