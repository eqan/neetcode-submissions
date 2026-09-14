class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        To give an example how hashmap works here is for example if we find element 3 we add it to the hashmap at index 0, when we find 4 and we subtract the target e.g 7 and it results in 3 we found that 2nd element which when summed with to get to the target
        Mind map formula -> needed_number=target − current_number = diff
        '''
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n # Complement formula, reversing the actual formula
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i