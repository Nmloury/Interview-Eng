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


class Solution2(object):
    def sorted_array_median(self, L):
        if len(L) % 2 == 0:
            return (L[len(L) / 2] + L[(len(L) / 2) - 1]) / 2.
        else:
            return L[len(L) / 2]


    def short_median(self, short, lon):
        s = short[0]
        n  = len(lon)
        lower = lon[n / 2  - 1]
        mid = lon[n / 2]
        upper = lon[n / 2  + 1]
        if n % 2 == 0:
            if s < lower:
                return lower
            elif s >= lower and s <= mid:
                return s
            else:
                return mid
        else:
            if s < lower:
                return (lower + mid) / 2.
            elif s >= lower and s <= upper:
                return (s + mid) / 2.
            else:
                return (upper + mid) / 2.

    def two_and_two(self, nums1, nums2):
        mx = max(nums1 + nums2)
        mn = min(nums1 + nums2)
        return (sum(nums1) + sum(nums2) - mx - mn) / 2.


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        med1 = self.sorted_array_median(nums1)
        med2 = self.sorted_array_median(nums2)
        if not nums1:
            return med2
        elif not nums2:
            return med1
        elif len(nums1) == 1:
            if len(nums2) == 2:
                return self.two_and_two(nums1, nums2) * 2
            else:
                return self.short_median(nums1, nums2)
        elif len(nums2) == 1:
            if len(nums1) == 2:
                return self.two_and_two(nums2, nums1) * 2
            else:
                return self.short_median(nums2, nums1)
        elif len(nums2) == 2 and len(nums1) == 2:
            return self.two_and_two(nums1, nums2)
        elif med1 == med2:
            return med1
        elif med1 > med2:
            return self.findMedianSortedArrays(nums1[:n / 2 + 1], nums2[m / 2:])
        else:
            return self.findMedianSortedArrays(nums1[n / 2:], nums2[:m / 2 + 1])
