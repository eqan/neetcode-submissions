class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = []
        for i in range(len(nums)):
            _sub_arrays = []
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum % k == 0:
                    count.append(1)
        return len(count)


        