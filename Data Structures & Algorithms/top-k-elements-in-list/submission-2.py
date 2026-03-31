class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        max_k = []
        i = 0
        for n in nums:
            count[n] += 1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for item in sorted_count.keys():
            if i >= k:
                return max_k
            else:
                max_k.append(item)
                i+=1
        return max_k