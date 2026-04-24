class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1
        
        arr = []

        for key, value in freq.items():
            arr.append([value,key])
        arr.sort()

        while k > 0:
            res.append(arr.pop()[1])
            k -= 1

        return res 
