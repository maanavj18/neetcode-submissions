class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = dict()
        mapT = dict()

        for x in s:
            if x not in mapS.keys():
                mapS.update({x:1})
            else:
                mapS[x] +=1

        for x in t:
            if x not in mapT.keys():
                mapT.update({x:1})
            else:
                mapT[x] +=1

        return mapS == mapT