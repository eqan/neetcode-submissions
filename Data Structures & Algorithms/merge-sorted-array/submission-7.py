class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        Whats happening here is, we start backwards from both arrays, whilst last is starting backwards from placeholders. We put the largest elements whether from nums1 or nums2 in the placeholders first. The nums1 array also gets modified inside as we had put the largest elements at the end so inbetween if we want to we can replace elements of nums1 with either smaller elements from nums2 or nums1 as the loop would break when num2 becomes 0.
        '''
        last = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[last] = nums1[i]
                i-=1
            else:
                nums1[last] = nums2[j]
                j-=1
            last -= 1
        return nums1

