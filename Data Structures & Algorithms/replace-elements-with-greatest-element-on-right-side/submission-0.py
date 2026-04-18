class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # right max = -1
        # Iterate array in reverse order
        # max = max(max, arr[i])
        rightMax = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
