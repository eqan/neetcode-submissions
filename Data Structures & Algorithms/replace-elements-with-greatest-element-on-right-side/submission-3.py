class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = -1
        for i in range(len(arr)-1, -1, -1):
            if k < arr[i]:
                tmp = arr[i]
                arr[i] = k
                k = tmp
            else:
                arr[i] = k
        return arr
