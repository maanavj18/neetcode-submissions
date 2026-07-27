class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            #i is the index of each number in the orignal nums
            result = [value * nums[i] if i != idx else value for idx, value in enumerate(result)]

        return result