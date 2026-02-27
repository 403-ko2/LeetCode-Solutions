class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _map = dict()

        for num in nums:
            if num in _map:
                return True
            _map[num] = True
        
        return False

      #alternative solution
        # nums.sort()

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True

        # return True if len(set(nums)) < len(nums) else False

                
