class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        maxRun = 0
        run = 0
        prev = -1 # -1 None | 0 Up | 1 Down
        for i in range(n - 1):
            if arr[i] < arr[i+1]:
                run = 1 + run if prev == 1 else 1
                prev = 0
            elif arr[i] > arr[i+1]:
                run = 1 + run if prev == 0 else 1
                prev = 1
            else:
                run = 0
                prev = -1
            maxRun = max(run, maxRun)
        return maxRun + 1
                

