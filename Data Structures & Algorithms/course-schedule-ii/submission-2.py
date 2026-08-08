class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preSet = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preSet[crs].append(pre)
        visit, cycle = set(), set()
        self.output = []
        def dfs(crs):
            if crs in visit:
                return True 
            if crs in cycle:
                return False 
                
            cycle.add(crs)
            for pre in preSet[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            self.output.append(crs)
            return True
       

        for c in range(numCourses):
            if not dfs(c):
                return []
        return self.output 
              
     
        

