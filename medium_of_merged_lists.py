from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pre_last = None
        last = None
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        a_merge_len = nums1_len + nums2_len
        current_len = 0
        need_len = (a_merge_len // 2) + 1
        just_last = True
        if a_merge_len % 2 == 0:
            just_last = False
        n1 = None
        n2 = None

        while (
                (nums1_len > 0 or n1 is not None)
                or (nums2_len > 0 or n2 is not None)) \
                and (current_len < need_len
        ):
            if n1 is None and nums1_len:
                n1 = nums1.pop(0)
                nums1_len -= 1
            if n2 is None and nums2_len:
                n2 = nums2.pop(0)
                nums2_len -= 1

            n1_ = n1 or 0
            n2_ = n2 or 0

            if (n2 is None or n1_ <= n2_) and n1 is not None:
                pre_last = last
                last = n1
                n1 = None
                current_len += 1
                if n1_ != n2_ or current_len >= need_len:
                    continue

            if (n1 is None or n2_ <= n1_) and n2 is not None:
                pre_last = last
                last = n2
                n2 = None
                current_len += 1

        if just_last:
            return last

        return (last + pre_last) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([100000], [100001]))
