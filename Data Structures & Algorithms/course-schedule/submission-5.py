class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.isTrue = False
        preSet = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preSet[crs].append(pre)
        visitSet = set()
        def dfs(crs):
            #means that we have identified a loop or a cycle in our graph
            if crs in visitSet:
                return False
            if preSet[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preSet[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preSet[crs] = []
            return True
        #think of this edge case (really hard)  
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


            