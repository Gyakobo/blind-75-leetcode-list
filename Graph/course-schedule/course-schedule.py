class Solution:
    def course_schedule(self, n, courses):
        # Create a dependency graph
        graph = {int:[]}
        
        graph = { i: for i in range(n)  }

        visited = set()

        def dfs(c):
            if c in visited:
                return False



        print(graph)

n = 6 
courses = [ [4, 5], [3, 4], [2, 3], [1, 2], [0, 1] ]
s = Solution()
print(s.course_schedule(n, courses)) 

