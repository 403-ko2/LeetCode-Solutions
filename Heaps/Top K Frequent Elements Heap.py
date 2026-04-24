
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        res = []
        heap = []

        for num in nums:
            freq[num] += 1

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res 
