class Solution:
    def course_schedule(self, numCourses, prerequisites):
        # Create a dependency graph
        preMap = {int:list}

        preMap = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            preMap[crs].append(pre)

        '''
        0: [1, 2] 
        1: [3, 4] 
        2: [] 
        3: [4] 
        4: [] 
        '''

        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        print(graph)
 
n = 5 
courses = [ [0, 1], [0, 2], [1, 3], [1, 4], [3, 4] ]
s = Solution()
print(s.course_schedule(n, courses)) 

