class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #{name, map, val}
        mapA = dict()
        for x in strs:
            mapX = dict()
            for y in x:
                if y in mapX.keys():
                    mapX[y]+=1
                else:
                    mapX.update({y:1})
                
            hashable = tuple(sorted(mapX.items()))
            print(hashable)
                
            if hashable in mapA.keys():
                mapA[hashable].append(x)
            else:
                mapA.update({hashable:[x]})

            
        return list(mapA.values())
            
           

            