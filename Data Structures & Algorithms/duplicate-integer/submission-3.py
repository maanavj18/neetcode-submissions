class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for x in nums:
            if(x in mySet):
                return True
            else:
                mySet.add(x)
        return False
            


        