class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}    

        for i in range(len(nums)):

            diff = target - nums[i]

            if nums[i] not in comp:
                comp[diff] = i
            else:
                return [comp[nums[i]], i]
        
        return []
                
        