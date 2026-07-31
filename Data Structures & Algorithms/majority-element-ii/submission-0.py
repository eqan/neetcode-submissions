class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        result = []
        for elem in nums:
            if elem not in counter.keys():
                counter[elem] = 1
            else:
                counter[elem] += 1
        n = len(nums)//3
        for k, v in counter.items():
            if v > n:
                result.append(k)
        return result

        