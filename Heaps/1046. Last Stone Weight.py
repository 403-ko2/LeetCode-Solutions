import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap) #negate the value of the weight to give us a max heap

        while len(heap) > 1:
            y = -1 * heapq.heappop(heap) #largest stone 
            x = -1 * heapq.heappop(heap) #second largest stone

            if x == y:
                continue

            heapq.heappush(heap, -1 * (y - x)) 
        
        if len(heap) == 0:
            return 0

        return -heap[0]
