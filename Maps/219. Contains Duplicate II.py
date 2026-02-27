class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        position = dict()

        for i, num in enumerate(nums):
            if num in position:
                if abs(position[num] - i) <= k:
                    return True
            position[num] = i
        
        return False
