class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [x for x, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
        
        
