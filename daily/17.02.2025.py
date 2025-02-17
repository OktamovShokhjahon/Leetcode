from itertools import combinations, permutations
class Solution:
    def numTilePossibilities(tiles: str) -> int:
        res=[]
        for i in range(1,len(tiles)+1):
            for j in permutations(tiles, i):
                if j not in res:
                    res.append(j)
        return len(res)
    print(numTilePossibilities("AAABBC"))