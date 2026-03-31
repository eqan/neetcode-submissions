class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l,r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            max_water = max(max_water, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water
            