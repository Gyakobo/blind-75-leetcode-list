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

        # visited = set()

        print(graph)
 
n = 5 
courses = [ [0, 1], [0, 2], [1, 3], [1, 4], [3, 4] ]
s = Solution()
print(s.course_schedule(n, courses)) 

