class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        n1, n2 = m - 1, n - 1
        while n2 > -1:
            if n1 >= 0 and nums2[n2] < nums1[n1]:
                nums1[last] = nums1[n1]
                n1-=1
            else:
                nums1[last] = nums2[n2]
                n2-=1
            last -=1
            

