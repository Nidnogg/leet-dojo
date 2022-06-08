class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        #move from end to beginning a.insert(0, a.pop(len(a)-1))
        p = list(range(1, m+1))
        result = []
        for i in range(len(queries)):
            result.append(p.index(queries[i]))
            p.insert(0, p.pop(p.index(queries[i])))
        return result
            