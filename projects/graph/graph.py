"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices!")
            
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # BFT Pseudocode
        # Create a queue
        queue = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        queue.enqueue(starting_vertex)
        # While: queue not empty
        while queue.size() > 0:
        # Pop first node out of queue
            vertex = queue.dequeue()
        # If not visited
            if vertex not in visited:
        #      Mark as visited
                visited.add(vertex)
                print(vertex)
        #      Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
        # Goto top of loop
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
                    
    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for next_vert in self.vertices[vertex]:
                self.dft_recursive(next_vert, visited)
        
        # # Class Solution
        # self, staring_vertex, visited=None
        # if visited is None:
        #     visited = set()
        # for child_vertex in self.vertices[starting_vertex]:
        #     if child_vertex not in visited:
        #         self.dft_recursive(child_vertex, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = []
        for vertex in self.vertices:
            unvisted = vertex

        starting_vertex.color = "gray"
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            visiting = queue[0]
            path = queue.dequeue()
            back_path = path[-1]

            if visiting == destination_vertex:
                return path

            for vertex in self.vertices[back_path]:
                if vertex.color == "white":
                    vertex.color = "gray"
                    queue.enqueue(vertex)

            visited.append()
        
        # # Class Solution
        # queue = Queue()
        # visited = set()
        # queue.enqueue([starting_vertex])
        # while queue.size() > 0:
        #     path = queue.dequeue()
        #     vertex = path[-1]
        #     if visited not in visited:
        #         # here is the point to do whatever is we are trying to accomplish
        #         if vertex == destination_vertex:
        #             return path
        #         visited.add(vertex)
        #         for next_vert in self.vertices[vertex]:
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             queue.enqueue(new_path)
            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # # Class Solution
        # stack = Stack()
        # visited = set()
        # stack.push([starting_vertex])
        # while stack.size() > 0:
        #     path = stack.pop()
        #     vertex = path[-1]
        #     if visited not in visited:
        #         # here is the point to do whatever is we are trying to accomplish
        #         if vertex == destination_vertex:
        #             return path
        #         visited.add(vertex)
        #         for next_vert in self.vertices[vertex]:
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             stack.push(new_path)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Starting DFT")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Starting BFT")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Starting DFT Recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS Paths")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS Paths")
    print(graph.dfs(1, 6))
