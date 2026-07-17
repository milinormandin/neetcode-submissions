class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}

        out = [None, None]

        for i in range(len(nums)):

            diff = target - nums[i]

            if nums[i] not in comp:
                comp[diff] = i
            else:
                out[0] = comp[nums[i]]
                out[1] = i
        
        return out
                
        