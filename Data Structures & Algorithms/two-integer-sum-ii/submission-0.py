class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        result = []
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            diff = target - (numbers[r] + numbers[l])

            if diff > 0:
                l+=1
                continue
            elif diff < 0:
                r-=1
                continue
            
            else:
                result = [l+1, r+1]
                return result
