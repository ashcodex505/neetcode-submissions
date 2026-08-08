class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preSet = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preSet[crs].append(pre)
        visitSet = set()
        def dfs(crs):
            if preSet[crs] == []:
                return True 
            if crs in visitSet:
                return False
            visitSet.add(crs)
            for pre in preSet[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preSet[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        


            