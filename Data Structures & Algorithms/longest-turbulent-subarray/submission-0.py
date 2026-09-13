class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        best = 0
        run = 0
        prev = -1  # -1 none, 0 UP, 1 DOWN

        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                run = run + 1 if prev == 1 else 1
                prev = 0
            elif arr[i] > arr[i + 1]:
                run = run + 1 if prev == 0 else 1
                prev = 1
            else:
                run = 0
                prev = -1
            best = max(best, run)

        return best + 1