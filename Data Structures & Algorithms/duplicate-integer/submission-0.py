class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counter_map = {}

        for num in nums:
            
            if num in counter_map:
                return True
            
            counter_map[num] = 1
        return False


