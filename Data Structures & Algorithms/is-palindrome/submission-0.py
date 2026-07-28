class Solution:
    def isPalindrome(self, s: str) -> bool:

        pt1 = 0
        pt2 = len(s) - 1





        while pt1 < pt2:
            if not s[pt1].isalnum():
                pt1+=1
                continue
            if not s[pt2].isalnum():
                pt2-=1
                continue
            elif s[pt1].lower() == s[pt2].lower():
                pt1+=1
                pt2-=1
            else:
                return False

        return True

            
            